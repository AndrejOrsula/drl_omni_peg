use drl_omni_peg::{env::drl_omni_peg_py, gymnasium};
use pyo3::{prelude::*, types::PyList};

const RENDER: bool = true;
const N_ENVS: usize = 8_usize.pow(2);
const DATASET: &str = "train";
const CURRICULUM_ACTIVE: bool = false;

fn main() -> pyo3::PyResult<()> {
    pyo3::append_to_inittab!(drl_omni_peg_py);

    pyo3::Python::with_gil(|py| {
        let env = make_env(py)?;
        let _reset_ret: &PyList = env.call_method0("reset")?.extract().unwrap();
        while env.call_method0("is_running")?.is_true()? {
            if !env.call_method0("is_playing")?.is_true()? {
                env.call_method0("update")?;
                continue;
            }
            let action_space: &gymnasium::Space =
                env.getattr("action_space").unwrap().extract().unwrap();
            let action: Vec<_> = (0..N_ENVS)
                .map(|_| action_space.sample(py, None).unwrap())
                .collect();
            let step_ret: &PyList = env
                .call_method1("step", (action,))
                .unwrap()
                .extract()
                .unwrap();
            if step_ret.iter().any(|ret| {
                let (_obs, _reward, terminated, truncated, _info) =
                    ret.extract::<(&PyAny, f32, bool, bool, &PyAny)>().unwrap();
                terminated || truncated
            }) {
                let _reset_ret: &PyList = env.call_method0("reset")?.extract().unwrap();
            }
        }

        Ok(())
    })
}

fn make_env(py: pyo3::prelude::Python<'_>) -> pyo3::PyResult<&pyo3::types::PyAny> {
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
        CURRICULUM_ACTIVE,
    ))?;

    // Start the timeline
    env.call_method0("start_timeline")?;

    Ok(env)
}
