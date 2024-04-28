use drl_omni_peg::{env::drl_omni_peg_py, stable_baselines3 as sb3};
use itertools::Itertools;
use pyo3::{prelude::*, types::PyDict};

const MODE: Mode = Mode::Train;
const RENDER: bool = false;
const N_ENVS: usize = 8_usize.pow(2);
const DATASET: &str = "train";
const CONTINUE_TRAINING: bool = true;
const DETERMINISTIC_EVAL: bool = false;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Mode {
    Train,
    Eval,
    Enjoy,
}

fn main() -> pyo3::PyResult<()> {
    pyo3::append_to_inittab!(drl_omni_peg_py);

    let logdir = std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("logdir")
        .join("ppo");

    pyo3::Python::with_gil(|py| {
        let device = "auto".to_object(py);

        match MODE {
            Mode::Train => {
                let env = wrap_env(py, make_env(py, true)?, &logdir)?;

                let policy = "MlpPolicy".to_object(py);
                let learning_rate = 0.0003_f64.into_py(py);
                let clip_range = 0.2_f64.into_py(py);
                let none = py.None();

                let policy_kwargs = PyDict::new(py);
                policy_kwargs.set_item("share_features_extractor", false)?;
                let net_arch = PyDict::new(py);
                net_arch.set_item("pi", vec![512, 512])?;
                net_arch.set_item("vf", vec![512, 512])?;
                policy_kwargs.set_item("net_arch", net_arch)?;
                // policy_kwargs.set_item("activation_fn", py.import("torch.nn")?.getattr("ReLU")?)?;

                let model_checkpoint = find_last_checkpoint(&logdir);
                let reset_num_timesteps = model_checkpoint.is_none();
                let agent = if let Some(load_model_path) = model_checkpoint {
                    println!("Loading model from {}", load_model_path.display());
                    sb3::ppo::PPO::load(
                        py,
                        &load_model_path,
                        env,
                        device.as_ref(py),
                        None,
                        false,
                        true,
                        None,
                    )?
                    .extract()?
                } else {
                    sb3::ppo::PPO::new(
                        py,
                        policy.as_ref(py),
                        env,
                        learning_rate.as_ref(py),
                        128,
                        (N_ENVS * 8) as i64,
                        8,
                        0.997,
                        0.95,
                        clip_range.as_ref(py),
                        none.as_ref(py),
                        true,
                        0.0003,
                        0.5,
                        0.5,
                        false,
                        -1,
                        None,
                        None,
                        None,
                        100,
                        None,
                        None,
                        1,
                        None,
                        device.as_ref(py),
                        true,
                    )?
                };

                let new_logger = sb3::common::logger::configure(
                    py,
                    Some(logdir.to_str().unwrap().to_owned()),
                    Some(vec![
                        "stdout".to_owned(),
                        "csv".to_owned(),
                        "tensorboard".to_owned(),
                    ]),
                )?;
                agent.call_method1("set_logger", (new_logger,))?;

                let checkpoint_callback = sb3::common::callbacks::CheckpointCallback::new(
                    py,
                    5_000,
                    logdir.to_str().unwrap(),
                    "rl_model",
                    false,
                    false,
                    1,
                )?;
                agent
                    .learn(
                        py,
                        100_000_000,
                        checkpoint_callback,
                        1,
                        "PPO",
                        reset_num_timesteps,
                        false,
                    )
                    .map_err(|e| {
                        e.print_and_set_sys_last_vars(py);
                    })
                    .unwrap();
                agent.call_method1("save", (logdir.join("model"),))?;
                env.call_method0("close")?;
            }

            Mode::Eval => {
                let env = wrap_env(py, make_env(py, false)?, &logdir)?;
                let load_model_path = find_last_checkpoint(&logdir).expect("No model to evaluate");
                let model = sb3::ppo::PPO::load(
                    py,
                    &load_model_path,
                    env,
                    device.as_ref(py),
                    None,
                    false,
                    true,
                    None,
                )?;
                let (mean_reward, std_reward): (f64, f64) =
                    sb3::common::evaluation::evaluate_policy(
                        py,
                        model,
                        env,
                        1_000_000,
                        DETERMINISTIC_EVAL,
                        false,
                        None,
                        None,
                        false,
                        true,
                    )?
                    .extract()?;
                println!("Mean reward: {mean_reward}, Std reward: {std_reward}");
            }

            Mode::Enjoy => {
                let env = wrap_env(py, make_env(py, false)?, &logdir)?;
                let load_model_path = find_last_checkpoint(&logdir).expect("No model to evaluate");
                let model = sb3::ppo::PPO::load(
                    py,
                    &load_model_path,
                    env,
                    device.as_ref(py),
                    None,
                    false,
                    true,
                    None,
                )?;

                let predict_kwargs = PyDict::new(py);
                predict_kwargs.set_item("deterministic", DETERMINISTIC_EVAL)?;

                let mut observation = env.call_method0("reset")?;
                loop {
                    let (action, _states) = model
                        .call_method("predict", (observation,), Some(predict_kwargs))?
                        .extract::<(&PyAny, &PyAny)>()?;

                    let (obs, _rew, _done, _info) = env
                        .call_method1("step", (action,))?
                        .extract::<(&PyAny, &PyAny, &PyAny, &PyAny)>()?;
                    observation = obs;
                }
            }
        }

        Ok(())
    })
}

fn find_last_checkpoint(logdir: &std::path::Path) -> Option<std::path::PathBuf> {
    if !CONTINUE_TRAINING || !logdir.is_dir() {
        return None;
    }

    // Load logdir/model.zip if exists
    if logdir.join("model.zip").exists() {
        return Some(logdir.join("model.zip"));
    }

    let checkpoints = logdir
        .read_dir()
        .unwrap()
        .filter_map(|entry| {
            entry.ok().and_then(|entry| {
                entry.file_name().into_string().ok().and_then(|file_name| {
                    file_name
                        .strip_prefix("rl_model_")
                        .and_then(|file_name| file_name.strip_suffix("_steps.zip"))
                        .and_then(|file_name| file_name.parse::<usize>().ok())
                })
            })
        })
        .collect_vec();

    if checkpoints.is_empty() {
        return None;
    }

    let last_checkpoint = checkpoints.iter().max().unwrap();
    Some(logdir.join(format!("rl_model_{last_checkpoint}_steps.zip")))
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
    logdir: &std::path::Path,
) -> pyo3::PyResult<&'py pyo3::types::PyAny> {
    const SB3_WRAPPER_CODE: &str = include_str!(concat!(
        env!("CARGO_MANIFEST_DIR"),
        "/src/python/sb3_wrapper.py"
    ));

    let env = PyModule::from_code(
        py,
        SB3_WRAPPER_CODE,
        concat!(env!("CARGO_MANIFEST_DIR"), "/src/python/sb3_wrapper.py"),
        "sb3_wrapper",
    )?
    .getattr("SingleProcessVecEnv")?
    .call1((env,))?;
    let env = sb3::common::vec_env::VecMonitor::new(
        py,
        env.extract()?,
        Some(logdir.join("monitor").to_str().unwrap().to_owned()),
        &["is_success".to_owned()],
    )?;

    env.extract()
}
