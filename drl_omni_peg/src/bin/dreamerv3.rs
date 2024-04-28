use drl_omni_peg::{dreamerv3, env::drl_omni_peg_py};
use pyo3::{
    prelude::*,
    types::{PyBool, PyDict, PyList},
};

const MODE: Mode = Mode::Train;
const RENDER: bool = false;
const N_ENVS: usize = 8_usize.pow(2);
const DATASET: &str = "train";

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Mode {
    Train,
    Eval,
}

fn main() -> pyo3::PyResult<()> {
    pyo3::append_to_inittab!(drl_omni_peg_py);

    pyo3::Python::with_gil(|py| {
        let config = config_dreamerv3(py, MODE == Mode::Train)?;

        // Create logdir directory
        let logdir: std::path::PathBuf = config.get_item("logdir")?.extract()?;
        std::fs::create_dir_all(&logdir)?;

        // Extract args passed for train/eval
        let args: &PyDict = config.get_item("run")?.extract()?;
        args.set_item("logdir", &logdir)?;
        args.set_item(
            "batch_steps",
            config.get_item("batch_size")?.extract::<u64>()?
                * config.get_item("batch_length")?.extract::<u64>()?,
        )?;
        if MODE == Mode::Train {
            args.set_item("from_checkpoint", logdir.join("checkpoint.ckpt"))?;
        }
        let args = dreamerv3::embodied::config::Config::new(py, (args,), None)?;

        let step = dreamerv3::embodied::Counter::new(py, 0)?;
        let outputs = PyList::new(
            py,
            [
                dreamerv3::embodied::logger::TensorBoardOutput::new(
                    py,
                    logdir.to_object(py).as_ref(py),
                    20,
                    1_000_000_000,
                    true,
                )?
                .extract::<&PyAny>()?,
                dreamerv3::embodied::logger::JSONLOutput::new(
                    py,
                    logdir.to_object(py).as_ref(py),
                    "metrics.jsonl",
                    ".*",
                    true,
                )?
                .extract()?,
            ],
        );
        let logger = dreamerv3::embodied::Logger::new(py, step, outputs, 1)?;

        match MODE {
            Mode::Train => {
                let env = wrap_env(py, make_env(py, true)?)?;

                let agent = dreamerv3::Agent::new(
                    py,
                    (env.obs_space(py)?, env.act_space(py)?, step, config),
                    None,
                )?;

                let samples_per_insert = py.None();
                let replay = dreamerv3::embodied::replay::Uniform::new(
                    py,
                    config.get_item("batch_length")?,
                    config.get_item("replay_size")?,
                    &logdir.join("replay"),
                    config.get_item("replay_online")?,
                    4096,
                    1,
                    samples_per_insert.as_ref(py),
                    10000,
                    0,
                )?;

                dreamerv3::embodied::run::train(py, agent, env, replay, logger, args)?;
            }

            Mode::Eval => {
                let env = wrap_env(py, make_env(py, false)?)?;

                let agent = dreamerv3::Agent::new(
                    py,
                    (env.obs_space(py)?, env.act_space(py)?, step, config),
                    None,
                )?;

                dreamerv3::embodied::run::eval_only(py, agent, env, logger, args).map_err(|e| {
                    e.print_and_set_sys_last_vars(py);
                    e
                })?;
            }
        }

        Ok(())
    })
}

fn make_env(
    py: pyo3::prelude::Python<'_>,
    curriculum_active: bool,
) -> pyo3::PyResult<&pyo3::types::PyAny> {
    let drl_omni_peg = PyModule::import(py, "drl_omni_peg_py")?;

    let env = drl_omni_peg.getattr("PyPegInHoleEnv")?.call1((
        std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"))
            .parent()
            .unwrap()
            .join("assets")
            .join(DATASET)
            .join("meshes"),
        N_ENVS,
        RENDER,
        curriculum_active,
    ))?;

    // Start the timeline
    env.call_method0("start_timeline")?;

    Ok(env)
}

fn wrap_env<'py>(
    py: pyo3::prelude::Python<'py>,
    env: &'py pyo3::types::PyAny,
) -> pyo3::PyResult<&'py dreamerv3::embodied::extracted_batch::ExtractedBatchEnv> {
    let env =
        dreamerv3::embodied::envs::FromGymnasiumParallel::new(py, env, "vector", "action", None)?;
    dreamerv3::embodied::extracted_batch::ExtractedBatchEnv::new(py, env)
}

fn config_dreamerv3(
    py: pyo3::prelude::Python<'_>,
    train: bool,
) -> Result<&dreamerv3::embodied::config::Config, pyo3::prelude::PyErr> {
    let config: &PyDict = dreamerv3::embodied::config::Config::new(
        py,
        (dreamerv3::configs(py)?.get_item("defaults")?.unwrap(),),
        None,
    )?
    .extract()?;

    config.set_item(
        "logdir",
        std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"))
            .parent()
            .unwrap()
            .join("logdir")
            .join("dreamerv3"),
    )?;
    config.set_item("jax.platform", "cpu")?;
    config.set_item("jax.precision", "float16")?;
    config.set_item("jax.prealloc", true)?;
    config.set_item("imag_horizon", 25)?;
    // encoder/decoder obs keys
    config.set_item("encoder.mlp_keys", "vector")?;
    config.set_item("decoder.mlp_keys", "vector")?;
    // encoder
    config.set_item("encoder.mlp_layers", 2)?;
    config.set_item("encoder.mlp_units", 512)?;
    // decoder
    config.set_item("decoder.mlp_layers", 2)?;
    config.set_item("decoder.mlp_units", 512)?;
    // rssm
    config.set_item("rssm.deter", 2048)?;
    config.set_item("rssm.units", 512)?;
    config.set_item("rssm.stoch", 32)?;
    config.set_item("rssm.classes", 32)?;
    // actor
    config.set_item("actor.layers", 2)?;
    config.set_item("actor.units", 512)?;
    // critic
    config.set_item("critic.layers", 2)?;
    config.set_item("critic.units", 512)?;
    // reward
    config.set_item("reward_head.layers", 2)?;
    config.set_item("reward_head.units", 512)?;
    // cont
    config.set_item("cont_head.layers", 2)?;
    config.set_item("cont_head.units", 512)?;
    // disag
    config.set_item("disag_head.layers", 2)?;
    config.set_item("disag_head.units", 512)?;
    // Learning rates
    config.set_item("model_opt.lr", 0.0001)?;
    config.set_item("actor_opt.lr", 0.00003)?;
    config.set_item("critic_opt.lr", 0.00003)?;

    config.set_item("run.log_keys_max", "is_success")?;

    if train {
        config.set_item("jax.platform", "gpu")?;
        config.set_item("envs.amount", N_ENVS)?;
        config.set_item("run.actor_batch", N_ENVS)?;
        config.set_item("replay_size", 20_000_000)?;
        config.set_item("run.steps", 100_000_000)?;
        config.set_item("run.log_every", 600)?;
        config.set_item("expl_behavior", "Random")?;
        config.set_item("run.expl_until", N_ENVS * 500)?;
        config.set_item("run.train_ratio", 8)?;
        config.set_item("batch_size", 16)?;
        config.set_item("batch_length", 64)?;
    } else {
        config.set_item("run.steps", 1_000_000_000)?;
    }

    let config = dreamerv3::embodied::Flags::new(py, (config,), None)?;
    let config = config.parse(py, PyList::empty(py), PyBool::new(py, true))?;
    config.extract()
}
