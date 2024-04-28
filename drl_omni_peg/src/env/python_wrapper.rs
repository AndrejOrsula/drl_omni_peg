use crate::env::peg_in_hole;
use crate::gymnasium;
use pyo3::prelude::*;

#[pymodule]
pub fn drl_omni_peg_py(_py: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_class::<PyPegInHoleEnv>()?;
    Ok(())
}

#[pyclass]
pub struct PyPegInHoleEnv(peg_in_hole::PegInHoleEnv);

#[pymethods]
impl PyPegInHoleEnv {
    #[new]
    pub fn py_new(
        mesh_dir: std::path::PathBuf,
        n_envs: usize,
        render: bool,
        curriculum_active: bool,
    ) -> PyResult<Self> {
        Ok(Self(peg_in_hole::PegInHoleEnv::new(
            mesh_dir,
            n_envs,
            render,
            curriculum_active,
        )))
    }

    #[getter]
    pub fn observation_space(&self) -> pyo3::PyResult<pyo3::Py<gymnasium::Space>> {
        Ok(self.0.observation_space.clone())
    }

    #[getter]
    pub fn action_space(&self) -> pyo3::PyResult<pyo3::Py<gymnasium::Space>> {
        Ok(self.0.action_space.clone())
    }

    #[getter]
    pub fn n_envs(&self) -> pyo3::PyResult<usize> {
        Ok(self.0.n_envs)
    }

    pub fn update(&mut self) {
        self.0.update()
    }

    pub fn step(
        &mut self,
        action: Vec<peg_in_hole::ActionSpace>,
    ) -> Vec<peg_in_hole::StepReturnType> {
        self.0.step(&action)
    }

    pub fn step_envs(
        &mut self,
        action: Vec<peg_in_hole::ActionSpace>,
        envs_to_process: Vec<usize>,
    ) -> Vec<peg_in_hole::StepReturnType> {
        self.0.step_envs(&action, &envs_to_process)
    }

    pub fn reset(&mut self) -> Vec<(peg_in_hole::ObservationSpaceStacked, peg_in_hole::InfoType)> {
        self.0.reset()
    }

    pub fn reset_envs(
        &mut self,
        envs_to_process: Vec<usize>,
    ) -> Vec<(peg_in_hole::ObservationSpaceStacked, peg_in_hole::InfoType)> {
        self.0.reset_envs(&envs_to_process)
    }

    pub fn start_timeline(&mut self) {
        self.0.start_timeline()
    }

    pub fn is_running(&mut self) -> bool {
        self.0.is_running()
    }

    pub fn is_playing(&mut self) -> bool {
        self.0.is_playing()
    }
}
