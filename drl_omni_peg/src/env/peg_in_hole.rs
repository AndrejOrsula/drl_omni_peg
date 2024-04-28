use crate::gymnasium;
use autocxx::WithinBox;
use omniverse::{omni, pxr, ToCppString};
use pxr::{TfToken, UsdTimeCode, VtValue};
use pyo3::IntoPy;
use rand::seq::SliceRandom;
use rand_distr::Distribution;
use std::{io::Write, ops::Deref, pin::Pin};

const EVAL: bool = true;
const EVAL_SHOWCASE: bool = false;
const EVAL_EPISODES_PER_ENV: usize = 1024;

/// Control of velocity in Cartesian space
/// - transX, transY, transZ, rotX, rotY, rotZ
pub type ActionSpace = [f32; 6];

// Metres
const ACTION_NOISE_TRANSLATION_STDDEV: f32 = 0.0005;
// Degrees
const ACTION_NOISE_ROTATION_STDDEV: f32 = 0.5;

/// Relative pose of the bottom of the peg with respect to the hole entrance (oriented with the flat surface of he module)
/// - ent_rel_posX, ent_rel_posY, ent_rel_posZ, ent_rel_rotXX, ent_rel_rotXX, ent_rel_rotZX, ent_rel_rotXY, ent_rel_rotXY, ent_rel_rotZY
/// Relative pose of the bottom of the peg with respect to the hole bottom (oriented with the hole)
/// - bot_rel_posX, bot_rel_posY, bot_rel_posZ, bot_rel_rotXX, bot_rel_rotXX, bot_rel_rotZX, bot_rel_rotXY, bot_rel_rotXY, bot_rel_rotZY
const OBSERVATION_LEN: usize = 18;
const N_OBSERVATION_STACKS: usize = 1;
pub type ObservationSpace = [f32; OBSERVATION_LEN];
pub type ObservationSpaceStacked = [f32; OBSERVATION_LEN * N_OBSERVATION_STACKS];

// Metres
const OBSERVATION_NOISE_TRANSLATION_STDDEV: f32 = 0.0005;
// Radians
const OBSERVATION_NOISE_ROTATION_STDDEV: f32 = 0.5 * (std::f32::consts::PI / 180.0);

/// Reward
pub type RewardType = f32;

/// Termination
/// Success:
/// - The bottom of the peg touches the bottom of the hole
/// Failure:
/// - The bottom of the peg is below the top of the module && outside of module XY boundaries + extra tolerance
pub type TerminationType = bool;

/// Truncation
/// Episode steps:
/// - Episode is longer than ~10 seconds
pub type TruncationType = bool;

pub type InfoType = rustc_hash::FxHashMap<String, bool>;

pub type StepReturnType = (
    ObservationSpaceStacked,
    RewardType,
    TerminationType,
    TruncationType,
    InfoType,
);
pub type ResetReturnType = (ObservationSpaceStacked, InfoType);

const TIME_STEPS_PER_SECOND: u32 = 200;
const CONTROL_HZ: u32 = 50;
const UPDATES_PER_STEP: u32 = TIME_STEPS_PER_SECOND / CONTROL_HZ;

/// Time limit of episode
const EPISODE_STEP_LIMIT: usize = 150;

const MODULE_SPACING: f32 = 0.15;

const USE_SDF_COLLISION_API: bool = true;
const SDF_RESOLUTION: i32 = 8;

const PHYSICS_DRIVE_AXES: [&str; 6] = ["transX", "transY", "transZ", "rotX", "rotY", "rotZ"];

const DRIVE_TYPE: &str = "effort";
const JOINT_DAMPING: f32 = 1.0;
const ACTION_SCALING_FACTOR_TRANSLATION: f32 = 0.25;
const ACTION_SCALING_FACTOR_ROTATION: f32 = 90.0;

const PEG_MASS: f32 = 0.2;

const SUCCESS_DISTANCE_THRESHOLD: f32 = 0.005;

const DISTANCE_TO_TARGET_TRANSLATION_WEIGHT: f32 = 0.8;
const DISTANCE_TO_TARGET_ROTATION_WEIGHT: f32 = 0.2;

const WORKSPACE_BOUNDARY_LENGTH: f32 = 0.3;
const WORKSPACE_BOUNDARY_LENGTH_BELOW_MODULE: f32 = 0.03;
const WORKSPACE_MAX_DISTANCE_BELOW_MODULE: f32 = 0.1;

const INITIAL_POSITION_RANDOM_RANGE: [f32; 3] = [0.5, 0.5, 0.1];
const INITIAL_POSITION_RANDOM_OFFSET_Z: f32 = 0.15;

const CURRICULUM_N_STEPS: usize = 50_000_000;

pub struct Curriculum {
    pub step_counter: usize,
    pub curriculum_active: bool,
}

impl Curriculum {
    pub fn new(curriculum_active: bool, _curriculum_inside_hole_active: bool) -> Self {
        Self {
            step_counter: 0,
            curriculum_active,
        }
    }
}

#[derive(Debug)]
pub struct EvalLogger {
    pub log_writer: Option<std::io::BufWriter<std::fs::File>>,

    pub n_resets: usize,

    pub current_episode_stats: Vec<EpisodeStats>,
    pub historical_episode_stats: Vec<Vec<EpisodeStats>>,
}

#[derive(Default, Debug, Clone, Copy)]
pub struct EpisodeStats {
    pub is_success: bool,
    pub is_truncated: bool,
    pub steps_until_success: usize,
}

impl EvalLogger {
    pub fn new(n_envs: usize) -> Self {
        let log_file_unique = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join(format!(
            "eval_log_{}-{}.csv",
            chrono::Local::now().format("%Y%m%d_%H%M%S"),
            rand::random::<u64>()
        ));
        println!(
            "Creating evaluation log file: {}",
            log_file_unique.display()
        );
        let log_file = std::fs::File::create(log_file_unique).unwrap();
        let mut log_writer = std::io::BufWriter::new(log_file);
        log_writer
            .write_all(b"env_id,is_success,is_truncated,steps_until_success\n")
            .unwrap();

        Self {
            log_writer: Some(log_writer),
            n_resets: 0,
            current_episode_stats: vec![Default::default(); n_envs],
            historical_episode_stats: vec![Default::default(); n_envs],
        }
    }
}

pub struct PegInHoleEnv {
    app: isaac_sim::SimulationApp,
    timeline: Pin<Box<omni::timeline::Timeline>>,
    stage: Pin<Box<pxr::UsdStageWeakPtr>>,

    /// Action space
    pub action_space: pyo3::Py<gymnasium::Space>,
    /// Observation space
    pub observation_space: pyo3::Py<gymnasium::Space>,
    observation_buffer: Vec<[ObservationSpace; N_OBSERVATION_STACKS]>,

    /// Paths to all meshes
    mesh_filepaths: Vec<std::path::PathBuf>,

    /// Number of environments
    pub n_envs: usize,

    /// Counter of steps in the environment
    step_counters: Vec<usize>,

    /// Default prim
    default_prim: Pin<Box<pxr::UsdPrim>>,
    /// List of prims for modules (n_envs long)
    module_prims: Vec<Pin<Box<pxr::UsdPrim>>>,
    hole_prims: Vec<Pin<Box<pxr::UsdPrim>>>,
    hole_entrance_paths: Vec<Pin<Box<pxr::SdfPath>>>,
    hole_bottom_paths: Vec<Pin<Box<pxr::SdfPath>>>,

    peg_prims: Vec<Pin<Box<pxr::UsdPrim>>>,
    /// List of peg joints
    peg_joints: Vec<Pin<Box<pxr::UsdPrim>>>,
    /// List of drives for each peg joint
    peg_drives: Vec<[Pin<Box<pxr::UsdPhysicsDriveAPI>>; 6]>,

    /// List of operations for transforming pegs (translation, rotation)
    peg_tranform_ops: Vec<[Pin<Box<pxr::UsdGeomXformOp>>; 2]>,

    // For reward computations
    initial_peg_to_hole_bottom_distances: Vec<f32>,
    completion_factor_peg_to_hole_bottom: Vec<f32>,

    curriculum: Curriculum,
    eval_logger: Option<EvalLogger>,
}

unsafe impl Send for PegInHoleEnv {}

impl PegInHoleEnv {
    pub fn new(
        mesh_dir: std::path::PathBuf,
        n_envs: usize,
        render: bool,
        curriculum_active: bool,
    ) -> Self {
        // Launch the simulation app
        let experience =
            std::path::Path::new(concat!(env!("CARGO_MANIFEST_DIR"), "/apps/omni.rust.kit"));
        let launch_config = omni::kit::AppDesc::builder()
            .experience(experience)
            .kit_args(
                omni::kit::AppDesc::kit_args_builder()
                    .headless(!render)
                    .ext_folder(isaac_sim::isaac_sim_path().join("apps"))
                    .ext_folder(isaac_sim::isaac_sim_path().join("exts"))
                    .ext_folder(isaac_sim::isaac_sim_path().join("extscache"))
                    .ext_folder(isaac_sim::isaac_sim_path().join("extsPhysics"))
                    .build(),
            )
            .build()
            .unwrap();
        let app = isaac_sim::SimulationApp::new(&launch_config).unwrap();
        let mut context = std::mem::ManuallyDrop::new(unsafe {
            Box::into_pin(Box::from_raw(omni::usd::UsdManager::createContext(
                &"".into_cpp(),
            )))
        });

        // Create timeline
        let timeline = context.getTimeline();
        let timeline: Pin<Box<omni::timeline::Timeline>> = unsafe {
            Box::into_pin(Box::from_raw(
                timeline.as_ref().unwrap() as *const _ as *mut _
            ))
        };

        let mut stage = if pxr::UsdUtilsStageCache::Get1().IsEmpty() {
            // Create a new stage if there is none yet
            let is_success = context.as_mut().newStage1();
            debug_assert!(is_success);
            let mut stage = context.as_mut().getStage().within_box();

            // Create World Xform and set it as default prim
            let world_prim = stage
                .as_deref_mut()
                .DefinePrim(
                    &pxr::SdfPath::new1(&"/World".into_cpp()).within_box(),
                    &pxr::TfToken::new3(&"Xform".into_cpp()).within_box(),
                )
                .within_box();
            stage.as_deref_mut().SetDefaultPrim(&world_prim);

            stage
        } else {
            // Otherwise, get the stage from the stage cache
            context.as_mut().getStage().within_box()
        };
        let default_prim = stage.as_mut().GetDefaultPrim().within_box();

        // Define physics scene (under Physics scope)
        let physics_path = default_prim
            .GetPath()
            .within_box()
            .AppendPath(&pxr::SdfPath::new1(&"Physics".into_cpp()).within_box())
            .within_box();
        let _physics = stage
            .as_deref_mut()
            .DefinePrim(
                &physics_path,
                &pxr::TfToken::new3(&"Scope".into_cpp()).within_box(),
            )
            .within_box();
        let physics_scene_path = physics_path
            .AppendPath(&pxr::SdfPath::new1(&"scene".into_cpp()).within_box())
            .within_box();
        let physics_scene =
            pxr::UsdPhysicsScene::Define(AsRef::as_ref(&stage), &physics_scene_path).within_box();
        let mut physics_scene_as_prim = stage.GetPrimAtPath(&physics_scene_path).within_box();

        // Looks scope
        let looks_path = default_prim
            .GetPath()
            .within_box()
            .AppendPath(&pxr::SdfPath::new1(&"Looks".into_cpp()).within_box())
            .within_box();
        let _looks = stage
            .as_deref_mut()
            .DefinePrim(
                &looks_path,
                &pxr::TfToken::new3(&"Scope".into_cpp()).within_box(),
            )
            .within_box();

        // Disable gravity
        let attr = physics_scene
            .CreateGravityMagnitudeAttr(&VtValue::from(0.0_f32), false)
            .within_box();
        attr.Set1(
            &VtValue::from(0.0_f32),
            pxr::UsdTimeCode::Default().within_box(),
        );
        let is_success = stage
            .GetPrimAtPath(&physics_scene_path)
            .within_box()
            .ApplyAPI(pxr::TfType::FindByName(
                &"PhysxSchemaPhysxSceneAPI".into_cpp(),
            ));
        debug_assert!(is_success);

        // Set solver type
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(&TfToken::new3(&"physxScene:solverType".into_cpp()).within_box())
            .within_box()
            .Set1(
                &VtValue::from(TfToken::new3(&"TGS".into_cpp()).within_box().deref()),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Enable CCD
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(&TfToken::new3(&"physxScene:enableCCD".into_cpp()).within_box())
            .within_box()
            .Set1(
                &VtValue::from(true),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Set friction offset threshold
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:frictionOffsetThreshold".into_cpp()).within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(0.005_f32),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Set friction correlation distance
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:frictionCorrelationDistance".into_cpp()).within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(0.001_f32),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Set GPU capacities
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:gpuTotalAggregatePairsCapacity".into_cpp())
                    .within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(10 * 1024_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:gpuFoundLostPairsCapacity".into_cpp()).within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(10 * 1024_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(&TfToken::new3(&"physxScene:gpuHeapCapacity".into_cpp()).within_box())
            .within_box()
            .Set1(
                &VtValue::from(64 * 1024 * 1024_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:gpuFoundLostAggregatePairsCapacity".into_cpp())
                    .within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(10 * 1024_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:gpuCollisionStackSize".into_cpp()).within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(64 * 1024 * 1024_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Set time step
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(&TfToken::new3(&"physxScene:timeStepsPerSecond".into_cpp()).within_box())
            .within_box()
            .Set1(
                &VtValue::from(TIME_STEPS_PER_SECOND),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Set min iteration count for position and velocity
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:minPositionIterationCount".into_cpp()).within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(4_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );
        physics_scene_as_prim
            .as_mut()
            .GetAttribute(
                &TfToken::new3(&"physxScene:minVelocityIterationCount".into_cpp()).within_box(),
            )
            .within_box()
            .Set1(
                &VtValue::from(1_u32),
                pxr::UsdTimeCode::Default().within_box(),
            );

        // Get list of all filepaths to meshes
        let mesh_filepaths = std::fs::read_dir(mesh_dir)
            .unwrap()
            .map(|res| res.map(|e| e.path()).unwrap())
            .collect();

        // Create observation and action spaces
        let (observation_space, action_space) = Self::define_spaces();

        let eval_logger = if EVAL {
            Some(EvalLogger::new(n_envs))
        } else {
            None
        };

        let mut env = Self {
            app,
            timeline,
            stage,
            action_space,
            observation_space,
            observation_buffer: vec![Default::default(); n_envs],
            mesh_filepaths,
            n_envs,
            step_counters: vec![0; n_envs],
            default_prim,
            module_prims: Vec::new(),
            hole_prims: Vec::new(),
            hole_entrance_paths: Vec::new(),
            hole_bottom_paths: Vec::new(),
            peg_prims: Vec::new(),
            peg_joints: Vec::new(),
            peg_drives: Vec::new(),
            peg_tranform_ops: Vec::new(),
            initial_peg_to_hole_bottom_distances: vec![-1.0; n_envs],
            completion_factor_peg_to_hole_bottom: vec![0.0; n_envs],
            curriculum: Curriculum::new(curriculum_active, false),
            eval_logger,
        };

        env.define_modules();
        env.filter_collisions();
        env.set_module_origins();

        env.apply_api_hole();
        env.apply_api_peg();

        env.create_peg_xform_ops();
        env.create_joints();

        if render {
            env.assign_random_visual_materials();
        }

        for i in 0..env.n_envs {
            env.assign_meshes(i);
        }

        env
    }

    pub fn update(&mut self) {
        self.app.update();
    }

    pub fn start_timeline(&mut self) {
        let start_time = self.timeline.timeToTimeCode(0.0);
        let end_time = self.timeline.timeToTimeCode(0.0);
        self.timeline.as_mut().play(start_time, end_time, false);

        // Run a single update step to initialize the simulation
        self.update();
    }

    pub fn is_running(&mut self) -> bool {
        self.app.is_running()
    }

    pub fn is_playing(&mut self) -> bool {
        self.timeline.isPlaying()
    }

    pub fn step(&mut self, action: &[ActionSpace]) -> Vec<StepReturnType> {
        let envs_to_process: Vec<_> = (0..self.n_envs).collect();
        self.step_envs(action, &envs_to_process)
    }

    pub fn step_envs(
        &mut self,
        action: &[ActionSpace],
        envs_to_process: &[usize],
    ) -> Vec<StepReturnType> {
        // Update curriculum
        if self.curriculum.curriculum_active {
            self.curriculum.step_counter += envs_to_process.len();
            if self.curriculum.step_counter >= CURRICULUM_N_STEPS {
                self.curriculum.curriculum_active = false;
            }
        }

        // Apply actions
        self.apply_actions(action, envs_to_process);

        // Update the simulation
        for _ in 0..UPDATES_PER_STEP {
            self.update();
        }

        let are_all_envs_done = if EVAL && !EVAL_SHOWCASE {
            let eval_logger = self.eval_logger.as_mut().unwrap();
            eval_logger
                .current_episode_stats
                .iter()
                .all(|stats| stats.is_success || stats.is_truncated)
        } else if EVAL_SHOWCASE {
            let eval_logger = self.eval_logger.as_mut().unwrap();
            eval_logger
                .current_episode_stats
                .iter()
                .any(|stats| stats.is_truncated)
        } else {
            false
        };

        // Extract states
        envs_to_process
            .iter()
            .map(|&i| {
                let (transform_peg_to_hole_entrance, transform_peg_to_hole_bottom) =
                    self.get_peg_transforms(i);

                // Extract observations from the transforms
                let obs =
                    Self::extract_obs(transform_peg_to_hole_entrance, transform_peg_to_hole_bottom);
                let obs = self.stack_obs(obs, i);

                // Reward
                let mut reward = self.compute_reward(transform_peg_to_hole_bottom, i);

                // Termination (success or failure)
                let (mut terminated, is_success) = self.check_if_terminated(
                    transform_peg_to_hole_entrance,
                    transform_peg_to_hole_bottom,
                );

                if terminated {
                    if is_success {
                        reward += 1.0 - self.completion_factor_peg_to_hole_bottom[i];
                    } else {
                        reward -= 1.0;
                    }
                }

                // Time limit truncation
                let truncated = self.update_is_truncated(i);

                // Info
                let mut info = rustc_hash::FxHashMap::default();
                info.insert("is_success".to_string(), is_success);

                if EVAL {
                    let eval_logger = self.eval_logger.as_mut().unwrap();
                    let current_episode_stats = &mut eval_logger.current_episode_stats[i];

                    if is_success && !current_episode_stats.is_success {
                        current_episode_stats.is_success = true;
                        current_episode_stats.steps_until_success = self.step_counters[i];
                    }

                    if truncated && !current_episode_stats.is_success {
                        current_episode_stats.is_truncated = true;
                    }

                    // Do not stop immediate if the episode terminates
                    if EVAL_SHOWCASE {
                        if are_all_envs_done {
                            terminated = true;
                        } else if is_success {
                            terminated = false;
                        }
                    } else if !are_all_envs_done {
                        terminated = false;
                    }
                }

                (obs, reward, terminated, truncated, info)
            })
            .collect()
    }

    pub fn reset(&mut self) -> Vec<ResetReturnType> {
        let envs_to_process: Vec<_> = (0..self.n_envs).collect();
        self.reset_envs(&envs_to_process)
    }

    pub fn reset_envs(&mut self, envs_to_process: &[usize]) -> Vec<ResetReturnType> {
        let mut episodes_to_write = Vec::default();

        // Disable velocities for environments that are to be reset
        self.apply_actions(&vec![[0.0; 6]; self.n_envs], envs_to_process);

        let ret = envs_to_process
            .iter()
            .map(|&i| {
                if EVAL {
                    let eval_logger = self.eval_logger.as_mut().unwrap();
                    let current_episode_stats = &mut eval_logger.current_episode_stats[i];
                    let historical_episode_stats = &mut eval_logger.historical_episode_stats[i];

                    if current_episode_stats.is_success || current_episode_stats.is_truncated {
                        historical_episode_stats.push(*current_episode_stats);
                        episodes_to_write.push((i, *current_episode_stats));
                        *current_episode_stats = Default::default();
                    }
                }

                // Reset step counter
                self.step_counters[i] = 0;

                // Reset the reward-related variables
                self.initial_peg_to_hole_bottom_distances[i] = -1.0;
                self.completion_factor_peg_to_hole_bottom[i] = 0.0;

                // Randomize the physics materials
                self.randomize_physics_material(i);

                // Randomize poses of pegs
                self.randomize_peg_pose(i);

                // Extract observations from the transforms
                let (transform_peg_to_hole_entrance, transform_peg_to_hole_bottom) =
                    self.get_peg_transforms(i);
                let obs =
                    Self::extract_obs(transform_peg_to_hole_entrance, transform_peg_to_hole_bottom);
                let obs = self.prefill_stacked_obs(obs, i);

                // Dummy info
                let info = rustc_hash::FxHashMap::default();

                (obs, info)
            })
            .collect();

        if EVAL {
            let eval_logger = self.eval_logger.as_mut().unwrap();
            let historical_episode_stats = &eval_logger.historical_episode_stats;
            let n_episodes = historical_episode_stats
                .iter()
                .map(|stats| stats.len() as u32)
                .sum::<u32>();
            if n_episodes > 0 {
                let log_writer = eval_logger.log_writer.as_mut().unwrap();
                for (i, episode_stats) in episodes_to_write.iter() {
                    log_writer
                        .write_all(
                            format!(
                                "{},{},{},{}\n",
                                i,
                                episode_stats.is_success as u8,
                                episode_stats.is_truncated as u8,
                                episode_stats.steps_until_success
                            )
                            .as_bytes(),
                        )
                        .unwrap();
                }
                log_writer.flush().unwrap();
                eval_logger.n_resets += 1;
                let n_successes = historical_episode_stats
                    .iter()
                    .map(|stats| stats.iter().filter(|stats| stats.is_success).count() as u32)
                    .sum::<u32>();
                let n_truncated = historical_episode_stats
                    .iter()
                    .map(|stats| stats.iter().filter(|stats| stats.is_truncated).count() as u32)
                    .sum::<u32>();

                let success_rate = n_successes as f32 / n_episodes as f32;
                let truncated_rate = n_truncated as f32 / n_episodes as f32;
                let mean_steps_until_success = if n_successes == 0 {
                    0.0
                } else {
                    historical_episode_stats
                        .iter()
                        .map(|stats| {
                            stats
                                .iter()
                                .filter(|stats| stats.is_success)
                                .map(|stats| stats.steps_until_success as f32)
                                .sum::<f32>()
                        })
                        .sum::<f32>()
                        / n_successes as f32
                };

                println!(
                "Episode {}/{} | Success rate: {:.2}%, Truncated rate: {:.2}%, Mean steps until success: {:.2} ({:.2} s)",
                eval_logger.n_resets,
                EVAL_EPISODES_PER_ENV,
                success_rate * 100.0,
                truncated_rate * 100.0,
                mean_steps_until_success,
                mean_steps_until_success / CONTROL_HZ as f32
            );
                if eval_logger.n_resets == EVAL_EPISODES_PER_ENV {
                    log_writer.write_all(b"\n").unwrap();
                    log_writer.flush().unwrap();

                    // Write success rate to another file
                    let success_rate_file =
                        std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join(format!(
                            "success_rate_{}-{}.csv",
                            chrono::Local::now().format("%Y%m%d_%H%M%S"),
                            rand::random::<u64>()
                        ));
                    println!(
                        "Creating success rate file: {}",
                        success_rate_file.display()
                    );
                    let success_rate_file = std::fs::File::create(success_rate_file).unwrap();
                    let mut success_rate_writer = std::io::BufWriter::new(success_rate_file);
                    success_rate_writer
                        .write_all(
                            format!(
                                "Total episodes: {}\nSuccess rate: {:.2}%\nTruncated rate: {:.2}%\nMean steps until success: {:.2} ({:.2} s)",
                                EVAL_EPISODES_PER_ENV,
                                success_rate * 100.0,
                                truncated_rate * 100.0,
                                mean_steps_until_success,
                                mean_steps_until_success / CONTROL_HZ as f32
                            )
                            .as_bytes(),
                        )
                        .unwrap();
                    success_rate_writer.flush().unwrap();

                    println!("All episodes done");
                    std::process::exit(0);
                }
            }
        }

        ret
    }

    fn define_spaces() -> (
        pyo3::prelude::Py<gymnasium::Space>,
        pyo3::prelude::Py<gymnasium::Space>,
    ) {
        let (observation_space, action_space) = pyo3::Python::with_gil(|py| {
            let none = py.None();
            let low = (-1.0_f32).into_py(py);
            let high = (1.0_f32).into_py(py);
            let t_f32 = py.import("numpy").unwrap().getattr("float32").unwrap();
            let observation_space = gymnasium::spaces::Box::new(
                py,
                low.as_ref(py),
                high.as_ref(py),
                Some(vec![(OBSERVATION_LEN * N_OBSERVATION_STACKS) as i64]),
                t_f32,
                none.as_ref(py),
            )
            .unwrap()
            .extract()
            .unwrap();
            let action_space = gymnasium::spaces::Box::new(
                py,
                low.as_ref(py),
                high.as_ref(py),
                Some(vec![6]),
                t_f32,
                none.as_ref(py),
            )
            .unwrap()
            .extract()
            .unwrap();

            (observation_space, action_space)
        });
        (observation_space, action_space)
    }

    fn apply_actions(&mut self, actions: &[ActionSpace], envs_to_process: &[usize]) {
        envs_to_process.iter().for_each(|&i| {
            for axis_i in 0..6 {
                let mut action = actions[i][axis_i].max(-1.0).min(1.0);
                if axis_i < 3 {
                    action *= ACTION_SCALING_FACTOR_TRANSLATION;

                    if ACTION_NOISE_TRANSLATION_STDDEV != 0.0 {
                        let normal =
                            rand_distr::Normal::new(0.0, ACTION_NOISE_TRANSLATION_STDDEV).unwrap();
                        action += normal.sample(&mut rand::thread_rng());
                    }
                } else {
                    action *= ACTION_SCALING_FACTOR_ROTATION;

                    if ACTION_NOISE_ROTATION_STDDEV != 0.0 {
                        let normal =
                            rand_distr::Normal::new(0.0, ACTION_NOISE_ROTATION_STDDEV).unwrap();
                        action += normal.sample(&mut rand::thread_rng());
                    }
                };

                self.peg_drives[i][axis_i]
                    .GetTargetVelocityAttr()
                    .within_box()
                    .Set1(
                        &pxr::VtValue::from(action),
                        pxr::UsdTimeCode::Default().within_box(),
                    );
            }
        });
    }

    fn extract_obs(
        transform_peg_to_hole_entrance: nalgebra::IsometryMatrix3<f32>,
        transform_peg_to_hole_bottom: nalgebra::IsometryMatrix3<f32>,
    ) -> ObservationSpace {
        let mut translation_peg_to_hole_entrance =
            transform_peg_to_hole_entrance.translation.vector;
        let mut translation_peg_to_hole_bottom = transform_peg_to_hole_bottom.translation.vector;

        if OBSERVATION_NOISE_TRANSLATION_STDDEV != 0.0 {
            let normal =
                rand_distr::Normal::new(0.0, OBSERVATION_NOISE_TRANSLATION_STDDEV).unwrap();
            normal
                .sample_iter(rand::thread_rng())
                .take(3)
                .enumerate()
                .for_each(|(i, noise)| {
                    translation_peg_to_hole_entrance[i] += noise;
                    translation_peg_to_hole_bottom[i] += noise;
                });
        }

        let mut rotation_peg_to_hole_entrance = transform_peg_to_hole_entrance.rotation;
        let mut rotation_peg_to_hole_bottom = transform_peg_to_hole_bottom.rotation;

        if OBSERVATION_NOISE_ROTATION_STDDEV != 0.0 {
            let normal = rand_distr::Normal::new(0.0, OBSERVATION_NOISE_ROTATION_STDDEV).unwrap();
            let orientation_offset = nalgebra::UnitQuaternion::from_axis_angle(
                &nalgebra::Unit::new_normalize(nalgebra::Vector3::new(
                    rand::random::<f32>() - 0.5,
                    rand::random::<f32>() - 0.5,
                    rand::random::<f32>() - 0.5,
                )),
                normal.sample(&mut rand::thread_rng()),
            )
            .to_rotation_matrix();
            rotation_peg_to_hole_entrance = orientation_offset * rotation_peg_to_hole_entrance;
            rotation_peg_to_hole_bottom = orientation_offset * rotation_peg_to_hole_bottom;
        }

        let rotation6d_peg_to_hole_entrance = rotation_peg_to_hole_entrance
            .matrix()
            .fixed_view::<3, 2>(0, 0);
        let rotation6d_peg_to_hole_bottom = rotation_peg_to_hole_bottom
            .matrix()
            .fixed_view::<3, 2>(0, 0);

        [
            translation_peg_to_hole_entrance.x,
            translation_peg_to_hole_entrance.y,
            translation_peg_to_hole_entrance.z,
            rotation6d_peg_to_hole_entrance[0],
            rotation6d_peg_to_hole_entrance[1],
            rotation6d_peg_to_hole_entrance[2],
            rotation6d_peg_to_hole_entrance[3],
            rotation6d_peg_to_hole_entrance[4],
            rotation6d_peg_to_hole_entrance[5],
            translation_peg_to_hole_bottom.x,
            translation_peg_to_hole_bottom.y,
            translation_peg_to_hole_bottom.z,
            rotation6d_peg_to_hole_bottom[0],
            rotation6d_peg_to_hole_bottom[1],
            rotation6d_peg_to_hole_bottom[2],
            rotation6d_peg_to_hole_bottom[3],
            rotation6d_peg_to_hole_bottom[4],
            rotation6d_peg_to_hole_bottom[5],
        ]
    }

    fn prefill_stacked_obs(
        &mut self,
        observation: ObservationSpace,
        i: usize,
    ) -> ObservationSpaceStacked {
        for j in 0..N_OBSERVATION_STACKS {
            self.observation_buffer[i][j] = observation;
        }
        self.observation_buffer[i].concat().try_into().unwrap()
    }

    fn stack_obs(&mut self, observation: ObservationSpace, i: usize) -> ObservationSpaceStacked {
        if N_OBSERVATION_STACKS > 1 {
            let previous_obs = self.observation_buffer[i][..(N_OBSERVATION_STACKS - 1)].to_owned();
            self.observation_buffer[i][1..].copy_from_slice(&previous_obs);
        }
        self.observation_buffer[i][0] = observation;
        self.observation_buffer[i].concat().try_into().unwrap()
    }

    fn compute_reward(
        &mut self,
        transform_peg_to_hole_bottom: nalgebra::IsometryMatrix3<f32>,
        i: usize,
    ) -> RewardType {
        // Compute reward based on the distance between the bottom of the peg and the bottom of the hole
        // The distance is computed as L2 norm of the error to the target pose
        let current_distance = Self::compute_distance_to_target(transform_peg_to_hole_bottom);

        // Set the initial distance if it has not been set yet (marked as negative)
        if self.initial_peg_to_hole_bottom_distances[i].is_sign_negative() {
            self.initial_peg_to_hole_bottom_distances[i] = current_distance;
        }

        // Compute the current completion percentage compared to the initial distance
        let current_completion_percentage =
            1.0 - (current_distance / self.initial_peg_to_hole_bottom_distances[i]).sqrt();

        // Compute difference to previous completion percentage
        let completion_percentage_delta =
            current_completion_percentage - self.completion_factor_peg_to_hole_bottom[i];

        // Update the completion percentage if it has increased
        self.completion_factor_peg_to_hole_bottom[i] = current_completion_percentage;

        // Return reward equal to progress towards the goal
        completion_percentage_delta
    }

    fn compute_distance_to_target(transform_to_target: nalgebra::IsometryMatrix3<f32>) -> f32 {
        // Compute distance to target pose
        let translation_distance = transform_to_target.translation.vector.norm();
        let rotation_distance =
            (transform_to_target.rotation.matrix() - nalgebra::Matrix3::<f32>::identity()).norm();

        DISTANCE_TO_TARGET_TRANSLATION_WEIGHT * translation_distance
            + DISTANCE_TO_TARGET_ROTATION_WEIGHT * rotation_distance
    }

    fn check_if_terminated(
        &mut self,
        transform_peg_to_hole_entrance: nalgebra::IsometryMatrix3<f32>,
        transform_peg_to_hole_bottom: nalgebra::IsometryMatrix3<f32>,
    ) -> (bool, bool) {
        let translation_distance = transform_peg_to_hole_bottom.translation.vector.norm();

        if translation_distance < SUCCESS_DISTANCE_THRESHOLD {
            // Terminate as success if the distance between the bottom of the peg and the bottom of the hole is below a threshold
            (true, true)
        } else if EVAL && !EVAL_SHOWCASE {
            // Keep running
            (false, false)
        } else {
            let offset = transform_peg_to_hole_entrance.translation.vector;

            if
            // Terminate if the positional offset is too large (too far away from the hole entrance)
            (offset.x.abs() > WORKSPACE_BOUNDARY_LENGTH
                || offset.y.abs() > WORKSPACE_BOUNDARY_LENGTH
                || offset.z > WORKSPACE_BOUNDARY_LENGTH) ||
                // Terminate if the peg is boing below the module
                (offset.z < -WORKSPACE_MAX_DISTANCE_BELOW_MODULE
                    && (offset.x.abs() > WORKSPACE_BOUNDARY_LENGTH_BELOW_MODULE
                        || offset.y.abs() > WORKSPACE_BOUNDARY_LENGTH_BELOW_MODULE))
            {
                (true, false)
            } else {
                // Otherwise, keep running
                (false, false)
            }
        }
    }

    fn update_is_truncated(&mut self, i: usize) -> bool {
        self.step_counters[i] += 1;
        self.step_counters[i] == EPISODE_STEP_LIMIT
    }

    fn define_modules(&mut self) {
        let xform_type_name = pxr::TfToken::new3(&"Xform".into_cpp()).within_box();
        for i in 0..self.n_envs {
            // Define module
            let module_path = self
                .default_prim
                .GetPath()
                .within_box()
                .AppendPath(
                    &pxr::SdfPath::new1(&format!("module_peg_in_hole_{i}").into_cpp()).within_box(),
                )
                .within_box();
            let module_prim = self
                .stage
                .as_deref_mut()
                .DefinePrim(&module_path, &xform_type_name)
                .within_box();
            self.module_prims.push(module_prim);

            // Define hole
            let hole_path = module_path
                .AppendPath(&pxr::SdfPath::new1(&"hole".into_cpp()).within_box())
                .within_box();
            let hole_prim = self
                .stage
                .as_deref_mut()
                .DefinePrim(&hole_path, &xform_type_name)
                .within_box();
            self.hole_prims.push(hole_prim);

            // Define paths to the hole entrance and bottom
            let hole_entrance_path = hole_path
                .AppendPath(&pxr::SdfPath::new1(&"entrance".into_cpp()).within_box())
                .within_box();
            let hole_bottom_path = hole_path
                .AppendPath(&pxr::SdfPath::new1(&"bottom".into_cpp()).within_box())
                .within_box();
            self.hole_entrance_paths.push(hole_entrance_path);
            self.hole_bottom_paths.push(hole_bottom_path);

            // Define peg
            let peg_path = module_path
                .AppendPath(&pxr::SdfPath::new1(&"peg".into_cpp()).within_box())
                .within_box();
            let peg_prim = self
                .stage
                .as_deref_mut()
                .DefinePrim(&peg_path, &xform_type_name)
                .within_box();
            self.peg_prims.push(peg_prim);
        }
    }

    fn filter_collisions(&mut self) {
        let collision_groups_path = self
            .default_prim
            .GetPath()
            .within_box()
            .AppendPath(&pxr::SdfPath::new1(&"Physics".into_cpp()).within_box())
            .within_box()
            .AppendPath(&pxr::SdfPath::new1(&"collision_groups".into_cpp()).within_box())
            .within_box();
        let _collision_goups = self
            .stage
            .as_deref_mut()
            .DefinePrim(
                &collision_groups_path,
                &pxr::TfToken::new3(&"Scope".into_cpp()).within_box(),
            )
            .within_box();

        for i in 0..self.n_envs {
            // Create a collision group
            let collision_group_path = collision_groups_path
                .AppendPath(&pxr::SdfPath::new1(&format!("group_{i}").into_cpp()).within_box())
                .within_box();
            let collision_group = pxr::UsdPhysicsCollisionGroup::Define(
                AsRef::as_ref(&self.stage),
                &collision_group_path,
            )
            .within_box();

            // Include the corresponding module
            let mut colliders_collection: std::pin::Pin<Box<pxr::UsdCollectionAPI>> =
                collision_group.GetCollidersCollectionAPI().within_box();
            let mut includes_relationship = colliders_collection
                .as_mut()
                .CreateIncludesRel()
                .within_box();
            includes_relationship.as_mut().AddTarget(
                &self.module_prims[i].GetPath().within_box(),
                pxr::UsdListPosition::UsdListPositionFrontOfAppendList,
            );

            // Filter collisions with all other modules
            let mut filtered_relationship = collision_group.CreateFilteredGroupsRel().within_box();
            (0..self.n_envs).filter(|j| i != *j).for_each(|j| {
                let collision_group_path = collision_groups_path
                    .AppendPath(&pxr::SdfPath::new1(&format!("group_{j}").into_cpp()).within_box())
                    .within_box();
                filtered_relationship.as_mut().AddTarget(
                    &collision_group_path,
                    pxr::UsdListPosition::UsdListPositionFrontOfAppendList,
                );
            });
        }
    }

    // Transform the peg-in-hole module into its position within a grid (similar to what cloner does)
    fn set_module_origins(&mut self) {
        let n_envs_sqrt = num_integer::sqrt(self.n_envs);

        for i in 0..self.n_envs {
            let location = pxr::GfVec3f::new2(
                (i % n_envs_sqrt) as f32 * MODULE_SPACING,
                (i / n_envs_sqrt) as f32 * MODULE_SPACING,
                0.0,
            )
            .within_box();
            let module_xform = pxr::UsdGeomXformable::new(&self.module_prims[i]).within_box();
            let mut translate_op = module_xform
                .AddTranslateOp(
                    pxr::UsdGeomXformOp_Precision::PrecisionFloat,
                    &pxr::TfToken::new().within_box(),
                    false,
                )
                .within_box();
            let res = translate_op.as_mut().set_vec3f(&location);
            debug_assert!(res);
        }
    }

    fn apply_api_hole(&mut self) {
        for i in 0..self.n_envs {
            // Add collision APIs for hole
            let _hole_collision_api =
                pxr::UsdPhysicsCollisionAPI::Apply(&self.hole_prims[i]).within_box();

            // Add physics material API for the hole
            let _hole_physics_material_api =
                pxr::UsdPhysicsMaterialAPI::Apply(&self.hole_prims[i]).within_box();
        }
    }

    fn apply_api_peg(&mut self) {
        for i in 0..self.n_envs {
            // Add collision APIs for peg
            let _peg_collision_api =
                pxr::UsdPhysicsCollisionAPI::Apply(&self.peg_prims[i]).within_box();
            let mut peg_mesh_collision_api =
                pxr::UsdPhysicsMeshCollisionAPI::Apply(&self.peg_prims[i]).within_box();

            if USE_SDF_COLLISION_API {
                // Use SDF collision approximation API
                let is_success = &self.peg_prims[i].ApplyAPI(pxr::TfType::FindByName(
                    &"PhysxSchemaPhysxSDFMeshCollisionAPI".into_cpp(),
                ));
                peg_mesh_collision_api
                    .as_mut()
                    .CreateApproximationAttr(
                        &VtValue::from(TfToken::new3(&"sdf".into_cpp()).within_box().deref()),
                        false,
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(TfToken::new3(&"sdf".into_cpp()).within_box().deref()),
                        pxr::UsdTimeCode::Default().within_box(),
                    );
                debug_assert!(is_success);

                // Set SDF resolution
                self.peg_prims[i]
                    .GetAttribute(
                        &TfToken::new3(&"physxSDFMeshCollision:sdfResolution".into_cpp())
                            .within_box(),
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(SDF_RESOLUTION),
                        pxr::UsdTimeCode::Default().within_box(),
                    );

                // Set SDF remeshing
                self.peg_prims[i]
                    .GetAttribute(
                        &TfToken::new3(&"physxSDFMeshCollision:sdfEnableRemeshing".into_cpp())
                            .within_box(),
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(false),
                        pxr::UsdTimeCode::Default().within_box(),
                    );

                // Set SDF margin
                self.peg_prims[i]
                    .GetAttribute(
                        &TfToken::new3(&"physxSDFMeshCollision:sdfBitsPerSubgridPixel".into_cpp())
                            .within_box(),
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(
                            TfToken::new3(&"BitsPerPixel32".into_cpp())
                                .within_box()
                                .deref(),
                        ),
                        pxr::UsdTimeCode::Default().within_box(),
                    );

                // Set SDF margin
                self.peg_prims[i]
                    .GetAttribute(
                        &TfToken::new3(&"physxSDFMeshCollision:sdfMargin".into_cpp()).within_box(),
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(0.0_f32),
                        pxr::UsdTimeCode::Default().within_box(),
                    );

                // Set SDF narrow band thickness
                self.peg_prims[i]
                    .GetAttribute(
                        &TfToken::new3(&"physxSDFMeshCollision:sdfNarrowBandThickness".into_cpp())
                            .within_box(),
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(0.0_f32),
                        pxr::UsdTimeCode::Default().within_box(),
                    );

                // Set SDF subgrid resolution
                self.peg_prims[i]
                    .GetAttribute(
                        &TfToken::new3(&"physxSDFMeshCollision:sdfSubgridResolution".into_cpp())
                            .within_box(),
                    )
                    .within_box()
                    .Set1(
                        &VtValue::from(0_i32),
                        pxr::UsdTimeCode::Default().within_box(),
                    );
            }

            // Add physics material API for the peg
            let _peg_physics_material_api =
                pxr::UsdPhysicsMaterialAPI::Apply(&self.peg_prims[i]).within_box();

            // Add rigid body APIs for the peg
            let _peg_rigid_body_api =
                pxr::UsdPhysicsRigidBodyAPI::Apply(&self.peg_prims[i]).within_box();
            let is_success = &self.peg_prims[i].ApplyAPI(pxr::TfType::FindByName(
                &"PhysxSchemaPhysxRigidBodyAPI".into_cpp(),
            ));
            debug_assert!(is_success);

            // Disable all damping and sleep/stabilization for the peg
            self.peg_prims[i]
                .GetAttribute(
                    &TfToken::new3(&"physxRigidBody:linearDamping".into_cpp()).within_box(),
                )
                .within_box()
                .Set1(
                    &VtValue::from(0.0_f32),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            self.peg_prims[i]
                .GetAttribute(
                    &TfToken::new3(&"physxRigidBody:angularDamping".into_cpp()).within_box(),
                )
                .within_box()
                .Set1(
                    &VtValue::from(0.0_f32),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            self.peg_prims[i]
                .GetAttribute(
                    &TfToken::new3(&"physxRigidBody:sleepThreshold".into_cpp()).within_box(),
                )
                .within_box()
                .Set1(
                    &VtValue::from(0.0_f32),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            self.peg_prims[i]
                .GetAttribute(
                    &TfToken::new3(&"physxRigidBody:stabilizationThreshold".into_cpp())
                        .within_box(),
                )
                .within_box()
                .Set1(
                    &VtValue::from(0.0_f32),
                    pxr::UsdTimeCode::Default().within_box(),
                );

            // Add mass APIs for peg
            let mut peg_mass_api = pxr::UsdPhysicsMassAPI::Apply(&self.peg_prims[i]).within_box();
            peg_mass_api
                .as_mut()
                .CreateMassAttr(&VtValue::from(PEG_MASS), false)
                .within_box()
                .Set1(
                    &VtValue::from(PEG_MASS),
                    pxr::UsdTimeCode::Default().within_box(),
                );
        }
    }

    fn create_peg_xform_ops(&mut self) {
        for i in 0..self.n_envs {
            let peg_xform = pxr::UsdGeomXformable::new(&self.peg_prims[i]).within_box();
            let translate_op = peg_xform
                .AddTranslateOp(
                    pxr::UsdGeomXformOp_Precision::PrecisionFloat,
                    &pxr::TfToken::new().within_box(),
                    false,
                )
                .within_box();
            let orient_op = peg_xform
                .AddOrientOp(
                    pxr::UsdGeomXformOp_Precision::PrecisionFloat,
                    &pxr::TfToken::new().within_box(),
                    false,
                )
                .within_box();
            self.peg_tranform_ops.push([translate_op, orient_op]);
        }
    }

    fn create_joints(&mut self) {
        for i in 0..self.n_envs {
            // Create a 6D joint from the module to the peg (to control the motion of the peg)
            let joint_path = self.peg_prims[i]
                .GetPath()
                .within_box()
                .AppendPath(&pxr::SdfPath::new1(&"joint".into_cpp()).within_box())
                .within_box();
            let mut joint =
                pxr::UsdPhysicsJoint::Define(AsRef::as_ref(&self.stage), &joint_path).within_box();
            joint.as_mut().CreateBody0Rel().within_box().AddTarget(
                &self.module_prims[i].GetPath().within_box(),
                pxr::UsdListPosition::UsdListPositionFrontOfPrependList,
            );
            joint.as_mut().CreateBody1Rel().within_box().AddTarget(
                &self.peg_prims[i].GetPath().within_box(),
                pxr::UsdListPosition::UsdListPositionFrontOfPrependList,
            );
            joint
                .as_mut()
                .CreateLocalPos0Attr(
                    &pxr::VtValue::from(pxr::GfVec3f::new2(0.0, 0.0, 0.0).within_box().deref()),
                    false,
                )
                .within_box()
                .Set1(
                    &pxr::VtValue::from(pxr::GfVec3f::new2(0.0, 0.0, 0.0).within_box().deref()),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            joint
                .as_mut()
                .CreateLocalRot0Attr(
                    &pxr::VtValue::from(
                        pxr::GfQuatf::new2(1.0, 0.0, 0.0, 0.0).within_box().deref(),
                    ),
                    false,
                )
                .within_box()
                .Set1(
                    &pxr::VtValue::from(
                        pxr::GfQuatf::new2(1.0, 0.0, 0.0, 0.0).within_box().deref(),
                    ),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            joint
                .as_mut()
                .CreateLocalPos1Attr(
                    &pxr::VtValue::from(pxr::GfVec3f::new2(0.0, 0.0, 0.0).within_box().deref()),
                    false,
                )
                .within_box()
                .Set1(
                    &pxr::VtValue::from(pxr::GfVec3f::new2(0.0, 0.0, 0.0).within_box().deref()),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            joint
                .as_mut()
                .CreateLocalRot1Attr(
                    &pxr::VtValue::from(
                        pxr::GfQuatf::new2(1.0, 0.0, 0.0, 0.0).within_box().deref(),
                    ),
                    false,
                )
                .within_box()
                .Set1(
                    &pxr::VtValue::from(
                        pxr::GfQuatf::new2(1.0, 0.0, 0.0, 0.0).within_box().deref(),
                    ),
                    pxr::UsdTimeCode::Default().within_box(),
                );

            // Enable collisions between the peg and the module (joint has collisions disabled by default)
            joint
                .CreateCollisionEnabledAttr(&VtValue::from(true), false)
                .within_box()
                .Set1(
                    &VtValue::from(true),
                    pxr::UsdTimeCode::Default().within_box(),
                );

            // Add drive APIs for the joint
            let joint_prim = self.stage.GetPrimAtPath(&joint_path).within_box();
            let joint_drives: Vec<_> = PHYSICS_DRIVE_AXES
                .iter()
                .map(|axis| {
                    let drive = pxr::UsdPhysicsDriveAPI::Apply(
                        &joint_prim,
                        &pxr::TfToken::new3(&axis.into_cpp()).within_box(),
                    )
                    .within_box();

                    // Set the type of the drive
                    drive
                        .CreateTypeAttr(
                            &pxr::VtValue::from(
                                pxr::TfToken::new3(&DRIVE_TYPE.into_cpp())
                                    .within_box()
                                    .deref(),
                            ),
                            false,
                        )
                        .within_box()
                        .Set1(
                            &pxr::VtValue::from(
                                pxr::TfToken::new3(&DRIVE_TYPE.into_cpp())
                                    .within_box()
                                    .deref(),
                            ),
                            pxr::UsdTimeCode::Default().within_box(),
                        );

                    // Set the damping of the drive
                    let damping = pxr::VtValue::from(JOINT_DAMPING);
                    drive
                        .CreateDampingAttr(&damping, false)
                        .within_box()
                        .Set1(&damping, pxr::UsdTimeCode::Default().within_box());

                    // Create target velocity interface
                    drive
                        .CreateTargetVelocityAttr(&pxr::VtValue::from(0.0_f32), false)
                        .within_box();

                    drive
                })
                .collect();
            let joint_drives = unsafe { joint_drives.try_into().unwrap_unchecked() };

            self.peg_joints.push(joint_prim);
            self.peg_drives.push(joint_drives);
        }
    }

    fn assign_meshes(&mut self, i: usize) {
        let mesh_path = if self.n_envs <= self.mesh_filepaths.len() {
            // Use i-th mesh in the list
            &self.mesh_filepaths[i]
        } else {
            // Select a random mesh
            self.mesh_filepaths.choose(&mut rand::thread_rng()).unwrap()
        };

        // Create and add a (mesh) reference for the hole
        self.hole_prims[i]
            .GetReferences()
            .within_box()
            .as_mut()
            .ClearReferences();
        let hole_reference = pxr::SdfReference::new(
            &mesh_path.to_string_lossy().into_cpp(),
            &pxr::SdfPath::new1(&"/module/hole".into_cpp()).within_box(),
            &pxr::SdfLayerOffset::new(0.0, 1.0).within_box(),
            &pxr::VtDictionary::new(),
        )
        .within_box();
        self.hole_prims[i]
            .GetReferences()
            .within_box()
            .as_mut()
            .AddReference(
                &hole_reference,
                pxr::UsdListPosition::UsdListPositionFrontOfAppendList,
            );

        // Create and add a (mesh) reference for the peg
        self.peg_prims[i]
            .GetReferences()
            .within_box()
            .as_mut()
            .ClearReferences();
        let peg_reference = pxr::SdfReference::new(
            &mesh_path.to_string_lossy().into_cpp(),
            &pxr::SdfPath::new1(&"/module/peg".into_cpp()).within_box(),
            &pxr::SdfLayerOffset::new(0.0, 1.0).within_box(),
            &pxr::VtDictionary::new(),
        )
        .within_box();
        self.peg_prims[i]
            .GetReferences()
            .within_box()
            .as_mut()
            .AddReference(
                &peg_reference,
                pxr::UsdListPosition::UsdListPositionFrontOfAppendList,
            );
    }

    fn assign_random_visual_materials(&mut self) {
        for i in 0..self.n_envs {
            let looks_path = self
                .default_prim
                .GetPath()
                .within_box()
                .AppendPath(&pxr::SdfPath::new1(&"Looks".into_cpp()).within_box())
                .within_box();

            let material_path = looks_path
                .AppendPath(&pxr::SdfPath::new1(&format!("material_{i}").into_cpp()).within_box())
                .within_box();
            let material =
                pxr::UsdShadeMaterial::Define(AsRef::as_ref(&self.stage), &material_path)
                    .within_box();

            let shared_path = material_path
                .AppendPath(&pxr::SdfPath::new1(&"shader".into_cpp()).within_box())
                .within_box();
            let mut shader =
                pxr::UsdShadeShader::Define(AsRef::as_ref(&self.stage), &shared_path).within_box();

            shader
                .CreateIdAttr(
                    &VtValue::from(
                        TfToken::new3(&"UsdPreviewSurface".into_cpp())
                            .within_box()
                            .deref(),
                    ),
                    false,
                )
                .within_box();
            shader
                .as_mut()
                .CreateInput(
                    &pxr::TfToken::new3(&"diffuseColor".into_cpp()).within_box(),
                    &pxr::SdfValueTypeNames::Color3f.into_value_type_name(),
                )
                .within_box()
                .Set(
                    &pxr::VtValue::from([
                        rand::random::<f32>(),
                        rand::random::<f32>(),
                        rand::random::<f32>(),
                    ]),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            shader
                .as_mut()
                .CreateInput(
                    &pxr::TfToken::new3(&"roughness".into_cpp()).within_box(),
                    &pxr::SdfValueTypeNames::Float.into_value_type_name(),
                )
                .within_box()
                .Set(
                    &pxr::VtValue::from(0.5_f32),
                    pxr::UsdTimeCode::Default().within_box(),
                );
            shader
                .as_mut()
                .CreateInput(
                    &pxr::TfToken::new3(&"metallic".into_cpp()).within_box(),
                    &pxr::SdfValueTypeNames::Float.into_value_type_name(),
                )
                .within_box()
                .Set(
                    &pxr::VtValue::from(0.0_f32),
                    pxr::UsdTimeCode::Default().within_box(),
                );

            let surface_output = material
                .CreateSurfaceOutput(&pxr::TfToken::new().within_box())
                .within_box();
            surface_output.ConnectToSource1(
                &shader.ConnectableAPI().within_box(),
                &pxr::TfToken::new3(&"surface".into_cpp()).within_box(),
                pxr::UsdShadeAttributeType::Output,
                &pxr::SdfValueTypeName::new().within_box(),
            );

            pxr::UsdShadeMaterialBindingAPI::Apply(&self.hole_prims[i])
                .within_box()
                .as_mut()
                .bind(&material);
            pxr::UsdShadeMaterialBindingAPI::Apply(&self.peg_prims[i])
                .within_box()
                .as_mut()
                .bind(&material);
        }
    }

    fn randomize_physics_material(&mut self, i: usize) {
        let mut hole_physics_material_api =
            pxr::UsdPhysicsMaterialAPI::new(&self.hole_prims[i]).within_box();
        let mut peg_physics_material_api =
            pxr::UsdPhysicsMaterialAPI::new(&self.peg_prims[i]).within_box();

        let static_friction = rand::random::<f32>();
        hole_physics_material_api
            .as_mut()
            .CreateStaticFrictionAttr(&VtValue::from(static_friction), false)
            .within_box()
            .Set1(
                &VtValue::from(static_friction),
                pxr::UsdTimeCode::Default().within_box(),
            );
        peg_physics_material_api
            .as_mut()
            .CreateStaticFrictionAttr(&VtValue::from(static_friction), false)
            .within_box()
            .Set1(
                &VtValue::from(static_friction),
                pxr::UsdTimeCode::Default().within_box(),
            );

        let dynamic_friction = rand::random::<f32>();
        hole_physics_material_api
            .as_mut()
            .CreateDynamicFrictionAttr(&VtValue::from(dynamic_friction), false)
            .within_box()
            .Set1(
                &VtValue::from(dynamic_friction),
                pxr::UsdTimeCode::Default().within_box(),
            );

        peg_physics_material_api
            .as_mut()
            .CreateDynamicFrictionAttr(&VtValue::from(dynamic_friction), false)
            .within_box()
            .Set1(
                &VtValue::from(dynamic_friction),
                pxr::UsdTimeCode::Default().within_box(),
            );

        let restitution = rand::random::<f32>();
        peg_physics_material_api
            .as_mut()
            .CreateRestitutionAttr(&VtValue::from(restitution), false)
            .within_box()
            .Set1(
                &VtValue::from(restitution),
                pxr::UsdTimeCode::Default().within_box(),
            );
        hole_physics_material_api
            .as_mut()
            .CreateRestitutionAttr(&VtValue::from(restitution), false)
            .within_box()
            .Set1(
                &VtValue::from(restitution),
                pxr::UsdTimeCode::Default().within_box(),
            );
    }

    fn randomize_peg_pose(&mut self, i: usize) {
        let hole_entrance_prim = self
            .stage
            .GetPrimAtPath(&self.hole_entrance_paths[i])
            .within_box();
        let hole_entrance_xform = pxr::UsdGeomXformable::new(&hole_entrance_prim).within_box();
        let hole_bottom_prim = self
            .stage
            .GetPrimAtPath(&self.hole_bottom_paths[i])
            .within_box();
        let hole_bottom_xform = pxr::UsdGeomXformable::new(&hole_bottom_prim).within_box();
        let transform_hole_entrance = Self::get_transform_as_isometry(&hole_entrance_xform);
        let transform_hole_bottom = Self::get_transform_as_isometry(&hole_bottom_xform);

        let mut position;
        let orientation;

        if self.curriculum.curriculum_active {
            let curriculum_progress_factor =
                self.curriculum.step_counter as f32 / CURRICULUM_N_STEPS as f32;

            // Add random translation and rotation equivalent to the curriculum progress
            position = transform_hole_entrance.translation.vector;
            position.x += (rand::random::<f32>() - 0.5)
                * curriculum_progress_factor
                * INITIAL_POSITION_RANDOM_RANGE[0];
            position.y += (rand::random::<f32>() - 0.5)
                * curriculum_progress_factor
                * INITIAL_POSITION_RANDOM_RANGE[1];
            position.z += (rand::random::<f32>())
                * curriculum_progress_factor
                * (INITIAL_POSITION_RANDOM_RANGE[2] + INITIAL_POSITION_RANDOM_OFFSET_Z);

            let orientation_offset = nalgebra::UnitQuaternion::from_axis_angle(
                &nalgebra::Unit::new_normalize(nalgebra::Vector3::new(
                    rand::random::<f32>() - 0.5,
                    rand::random::<f32>() - 0.5,
                    rand::random::<f32>() - 0.5,
                )),
                curriculum_progress_factor * std::f32::consts::PI,
            );
            orientation =
                nalgebra::UnitQuaternion::from_rotation_matrix(&transform_hole_bottom.rotation)
                    * orientation_offset;
        } else {
            position = transform_hole_entrance.translation.vector;
            position.x += (rand::random::<f32>() - 0.5) * INITIAL_POSITION_RANDOM_RANGE[0];
            position.y += (rand::random::<f32>() - 0.5) * INITIAL_POSITION_RANDOM_RANGE[1];
            position.z += (rand::random::<f32>()) * INITIAL_POSITION_RANDOM_RANGE[2]
                + INITIAL_POSITION_RANDOM_OFFSET_Z;

            let orientation_offset = nalgebra::UnitQuaternion::from_axis_angle(
                &nalgebra::Unit::new_normalize(nalgebra::Vector3::new(
                    rand::random::<f32>() - 0.5,
                    rand::random::<f32>() - 0.5,
                    rand::random::<f32>() - 0.5,
                )),
                rand::random::<f32>() * std::f32::consts::PI,
            );
            orientation = orientation_offset;
        }

        let position = pxr::GfVec3f::new2(position.x, position.y, position.z).within_box();
        let res = self.peg_tranform_ops[i][0].as_mut().set_vec3f(&position);
        debug_assert!(res);

        let orientation =
            pxr::GfQuatf::new2(orientation.w, orientation.i, orientation.j, orientation.k)
                .within_box();
        let res = self.peg_tranform_ops[i][1].as_mut().set_quatf(&orientation);
        debug_assert!(res);
    }

    fn get_peg_transforms(
        &mut self,
        i: usize,
    ) -> (
        nalgebra::IsometryMatrix3<f32>,
        nalgebra::IsometryMatrix3<f32>,
    ) {
        let peg_xform = pxr::UsdGeomXformable::new(&self.peg_prims[i]).within_box();

        let hole_entrance_prim = self
            .stage
            .GetPrimAtPath(&self.hole_entrance_paths[i])
            .within_box();
        let hole_entrance_xform = pxr::UsdGeomXformable::new(&hole_entrance_prim).within_box();

        let hole_bottom_prim = self
            .stage
            .GetPrimAtPath(&self.hole_bottom_paths[i])
            .within_box();
        let hole_bottom_xform = pxr::UsdGeomXformable::new(&hole_bottom_prim).within_box();

        let transform_peg = Self::get_transform_as_isometry(&peg_xform);
        let transform_hole_entrance = Self::get_transform_as_isometry(&hole_entrance_xform);
        let transform_hole_bottom = Self::get_transform_as_isometry(&hole_bottom_xform);

        let transform_peg_to_hole_entrance = transform_hole_entrance.inv_mul(&transform_peg);
        let transform_peg_to_hole_bottom = transform_hole_bottom.inv_mul(&transform_peg);

        (transform_peg_to_hole_entrance, transform_peg_to_hole_bottom)
    }

    fn get_transform_as_isometry(
        xformable: &pxr::UsdGeomXformable,
    ) -> nalgebra::IsometryMatrix3<f32> {
        // Get the transform of the peg
        let mut transform = pxr::GfMatrix4d::new().within_box();
        let mut resetsxformstack = false;
        let is_success = unsafe {
            xformable.GetLocalTransformation(
                std::mem::transmute(transform.as_mut()),
                &mut resetsxformstack,
                UsdTimeCode::Default().within_box(),
            )
        };
        debug_assert!(is_success);

        // Convert to nalgebra
        let matrix = unsafe { std::slice::from_raw_parts(transform.data1(), 16) };
        let matrix = nalgebra::Matrix4::from_column_slice(matrix);
        nalgebra::IsometryMatrix3::from_parts(
            nalgebra::Translation3::from(matrix.column(3).xyz()),
            nalgebra::Rotation3::from_matrix_unchecked(
                matrix.fixed_view::<3, 3>(0, 0).into_owned(),
            ),
        )
        .cast()
    }
}
