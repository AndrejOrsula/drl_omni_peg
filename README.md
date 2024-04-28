# Leveraging Procedural Generation for Learning Autonomous Peg-in-Hole Assembly in Space

This project focuses on learning autonomous peg-in-hole assembly with deep reinforcement learning, with a particular emphasis on enhancing generalization and adaptability through procedural generation and domain randomization.

<p align="center" float="middle">
  <img width="100.0%" src="https://github.com/AndrejOrsula/procgen_for_peg_in_hole_assembly/raw/main/media/sac_in_training.webp"/>
  <em>SAC agent collecting experience during training.</em>
</p>

<p align="center" float="middle">
  <img width="50.0%" src="https://github.com/AndrejOrsula/procgen_for_peg_in_hole_assembly/raw/main/media/dreamerv3_eval_test_set.webp"/><img width="50.0%" src="https://github.com/AndrejOrsula/procgen_for_peg_in_hole_assembly/raw/main/media/dreamerv3_eval_profiles.webp"/>
  <em>DreamerV3 agent evaluated on novel test set and assembly scenarios.</em>
</p>

## Overview

<p align="center">
  <a href="https://www.blender.org">
    <img src="https://img.shields.io/badge/Procedural%20Generation-Blender-F4792B"/>
  </a>
  <a href="https://www.nvidia.com/en-us/omniverse">
    <img src="https://img.shields.io/badge/Robotics%20Simulator-NVIDIA%20Omniverse-76B900"/>
  </a>
  <br>
  <a href="https://gymnasium.farama.org">
    <img src="https://img.shields.io/badge/Environment%20API-Gymnasium-CBCBCC"/>
  </a>
  <a href="https://stable-baselines3.readthedocs.io">
    <img src="https://img.shields.io/badge/Model--Free%20RL-Stable--Baselines3-BDF25E"/>
  </a>
  <a href="https://danijar.com/project/dreamerv3">
    <img src="https://img.shields.io/badge/Model--Based%20RL-DreamerV3-0053D6"/>
  </a>
</p>

As a proof-of-concept, the [environment logic](drl_omni_peg/src/env/peg_in_hole.rs) and training/evaluation pipelines are implemented in Rust. Blender's Geometry Nodes are used for procedural generation of peg-in-hole modules via [blr](https://github.com/AndrejOrsula/blr). NVIDIA Omniverse is used as the simulation backend through [omniverse_rs](https://github.com/AndrejOrsula/omniverse_rs) and [pxr_rs](https://github.com/AndrejOrsula/pxr_rs) for USD-related utilities. Gymnasium API is exposed by [gymnasium_rs](https://github.com/AndrejOrsula/gymnasium_rs). Lastly, interfacing with Stable-Baselines3 and DreamerV3 is accomplished with Rust bindings that are automatically generated by [pyo3_bindgen](https://github.com/AndrejOrsula/pyo3_bindgen).

The workspace contains these packages:

- **[drl_omni_peg](drl_omni_peg):** Peg-in-hole environment and RL training/evaluation pipelines
- **[procgen_peg_in_hole](procgen_peg_in_hole):** Procedural pipelines for generating peg-in-hole modules

## Instructions

### <a href="#-rust"><img src="https://rustacean.net/assets/rustacean-flat-noshadow.svg" width="16" height="16"></a> Rust

> \[!TIP\]
> You can install Rust and Cargo through your package manager or via <https://rustup.rs>.

#### Generation of Procedural Peg-in-Hole Modules

The train and test sets can be generated via [`generate_peg_in_hole_train.rs`](procgen_peg_in_hole/src/bin/generate_peg_in_hole_train.rs) and [`generate_peg_in_hole_test.rs`](procgen_peg_in_hole/src/bin/generate_peg_in_hole_test.rs), respectively.

```bash
# Generate train set
cargo run --release --bin generate_peg_in_hole_train
# Generate test set
cargo run --release --bin generate_peg_in_hole_test
```

#### Random Agent

A random agent can be run either via [`random.rs`](drl_omni_peg/src/bin/random.rs) or [`random_gymnasium.rs`](drl_omni_peg/src/bin/random_gymnasium.rs). The former uses the environment directly, while the latter goes through the Gymnasium API.

```bash
# Run random agent
cargo run --release --bin random
# (alternative) Run random agent through Gymnasium API
cargo run --release --bin random_gymnasium
```

#### Training and Evaluation of RL Agents

Each algorithm is implemented as a separate binary. You can edit the source code directly to modify the hyperparameters and change the training/evaluation pipeline. Pre-trained models are available for download [here](https://drive.google.com/drive/folders/1WmPzUMm2zM5FLCS04aUT0-HNkaUVh7wd).

- [`dreamerv3.rs`](drl_omni_peg/src/bin/dreamerv3.rs)
- [`ppo.rs`](drl_omni_peg/src/bin/ppo.rs)
- [`ppo_recurrent.rs`](drl_omni_peg/src/bin/ppo_recurrent.rs)
- [`sac.rs`](drl_omni_peg/src/bin/sac.rs)
- [`tqc.rs`](drl_omni_peg/src/bin/tqc.rs)
- [`trpo.rs`](drl_omni_peg/src/bin/trpo.rs)

```bash
# ALGO in [dreamerv3, ppo, ppo_recurrent, sac, tqc, trpo]
cargo run --release --bin ALGO
```

<details>
<summary><h3><a href="#-docker"><img src="https://www.svgrepo.com/show/448221/docker.svg" width="16" height="16"></a> Docker</h3></summary>

> To install [Docker](https://docs.docker.com/get-docker) on your system, you can run [`.docker/host/install_docker.bash`](.docker/host/install_docker.bash) to configure Docker with NVIDIA GPU support.
>
> ```bash
> .docker/host/install_docker.bash
> ```

#### Build Image

To build a new Docker image from [`Dockerfile`](Dockerfile), you can run [`.docker/build.bash`](.docker/build.bash) as shown below.

```bash
.docker/build.bash ${TAG:-latest} ${BUILD_ARGS}
```

#### Run Container

To run the Docker container, you can use [`.docker/run.bash`](.docker/run.bash) as shown below.

```bash
.docker/run.bash ${TAG:-latest} ${CMD}
```

#### Run Dev Container

To run the Docker container in a development mode (source code mounted as a volume), you can use [`.docker/dev.bash`](.docker/dev.bash) as shown below.

```bash
.docker/dev.bash ${TAG:-latest} ${CMD}
```

As an alternative, users familiar with [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) can modify the included [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json) to their needs. For convenience, [`.devcontainer/open.bash`](.devcontainer/open.bash) script is available to open this repository as a Dev Container in VS Code.

```bash
.devcontainer/open.bash
```

#### Join Container

To join a running Docker container from another terminal, you can use [`.docker/join.bash`](.docker/join.bash) as shown below.

```bash
.docker/join.bash ${CMD:-bash}
```

</details>

## Citation

```bibtex
@inproceedings{orsula2024leveraging,
  author    = {Andrej Orsula and Matthieu Geist and Miguel Olivares-Mendez and Carol Martinez},
  title     = {{Leveraging Procedural Generation for Learning Autonomous Peg-in-Hole Assembly in Space}},
  year      = {2024},
  booktitle = {International Conference on Space Robotics (iSpaRo)},
}
```

## License

This project is dual-licensed to be compatible with the Rust project, under either the [MIT](LICENSE-MIT) or [Apache 2.0](LICENSE-APACHE) licenses.
