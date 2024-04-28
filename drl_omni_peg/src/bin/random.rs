use drl_omni_peg::env::PegInHoleEnv;

const RENDER: bool = true;
const N_ENVS: usize = 8_usize.pow(2);
const DATASET: &str = "train";
const CURRICULUM_ACTIVE: bool = false;

fn main() {
    let mut env = PegInHoleEnv::new(
        std::path::PathBuf::from(env!("CARGO_MANIFEST_DIR"))
            .parent()
            .unwrap()
            .join("assets")
            .join(DATASET)
            .join("meshes"),
        N_ENVS,
        RENDER,
        CURRICULUM_ACTIVE,
    );

    // Start the timeline
    env.start_timeline();

    let _reset_ret = env.reset();
    let mut envs_to_reset = Vec::with_capacity(N_ENVS);
    while env.is_running() {
        if !env.is_playing() {
            env.update();
            continue;
        }

        if !envs_to_reset.is_empty() {
            let _reset_ret = env.reset_envs(&envs_to_reset);
            envs_to_reset.clear();
        }

        let action: Vec<_> = (0..N_ENVS)
            .map(|_| {
                std::iter::repeat_with(|| 2.0 * (rand::random::<f32>() - 0.5))
                    .take(6)
                    .collect::<Vec<_>>()
                    .try_into()
                    .unwrap()
            })
            .collect();
        let step_ret = env.step(&action);

        step_ret.iter().enumerate().for_each(
            |(i, (_obs, _reward, terminated, truncated, _info))| {
                if *terminated || *truncated {
                    envs_to_reset.push(i);
                }
            },
        );
    }
}
