### Isaac Sim image <https://catalog.ngc.nvidia.com/orgs/nvidia/containers/isaac-sim>
ARG ISAAC_SIM_IMAGE_NAME="nvcr.io/nvidia/isaac-sim"
ARG ISAAC_SIM_IMAGE_TAG="2023.1.1"

### Base image <https://hub.docker.com/_/ubuntu>
ARG BASE_IMAGE_NAME="ubuntu"
ARG BASE_IMAGE_TAG="jammy"

FROM ${ISAAC_SIM_IMAGE_NAME}:${ISAAC_SIM_IMAGE_TAG} AS isaac_sim
FROM ${BASE_IMAGE_NAME}:${BASE_IMAGE_TAG} AS base

### Use bash as the default shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

### Create a barebones entrypoint that is conditionally updated throughout the Dockerfile
RUN echo "#!/usr/bin/env bash" >> /entrypoint.bash && \
    chmod +x /entrypoint.bash

### Build OpenUSD
ARG OPENUSD_VERSION="22.11"
COPY ./.docker/internal/pxr_sys/patches/src/build_scripts/build_usd.py.patch /tmp/build_usd.py.patch
# hadolint ignore=SC2016
RUN OPENUSD_DL_PATH="/tmp/OpenUSD-${OPENUSD_VERSION}.tar.gz" && \
    OPENUSD_SRC_DIR="/tmp/OpenUSD-${OPENUSD_VERSION}" && \
    OPENUSD_INSTALL_DIR="${HOME}/openusd" && \
    echo -e "\n# OpenUSD ${OPENUSD_VERSION}" >> /entrypoint.bash && \
    echo "export OPENUSD_PATH=\"${OPENUSD_INSTALL_DIR}\"" >> /entrypoint.bash && \
    echo '# export PATH="${OPENUSD_PATH}/bin${PATH:+:${PATH}}"' >> /entrypoint.bash && \
    echo '# export LD_LIBRARY_PATH="${OPENUSD_PATH}/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"' >> /entrypoint.bash && \
    echo '# export PYTHONPATH="${OPENUSD_PATH}/lib/python${PYTHONPATH:+:${PYTHONPATH}}"' >> /entrypoint.bash && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    build-essential \
    ca-certificates \
    clang \
    cmake \
    curl \
    libarchive-dev \
    libgl-dev \
    libglfw3-dev \
    libglib2.0-dev \
    libglu-dev \
    libglu1-mesa-dev \
    libilmbase-dev \
    libssl-dev \
    libtbb2-dev \
    libx11-dev \
    libxt-dev \
    pkg-config \
    python3-dev \
    python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir PyOpenGL==3.1.7 pyside6==6.6.0 && \
    curl --proto "=https" --tlsv1.2 -sSfL "https://github.com/PixarAnimationStudios/OpenUSD/archive/refs/tags/v${OPENUSD_VERSION}.tar.gz" -o "${OPENUSD_DL_PATH}" && \
    mkdir -p "${OPENUSD_SRC_DIR}" && \
    tar xf "${OPENUSD_DL_PATH}" -C "${OPENUSD_SRC_DIR}" --strip-components=1 && \
    rm "${OPENUSD_DL_PATH}" && \
    if [[ "${OPENUSD_VERSION}" = "22.11" ]]; then \
    patch --unified --strip=1 --batch --follow-symlinks --ignore-whitespace --input=/tmp/build_usd.py.patch --directory="${OPENUSD_SRC_DIR}" ; \
    fi && \
    rm /tmp/build_usd.py.patch && \
    python3 "${OPENUSD_SRC_DIR}/build_scripts/build_usd.py" \
    --build-shared \
    --build-variant=release --prefer-speed-over-safety \
    --use-cxx11-abi=0 \
    --build-args USD,"-DPXR_LIB_PREFIX=lib" \
    --no-tests --no-examples --no-tutorials --no-tools --no-docs \
    --usdview \
    --python --no-debug-python \
    --usd-imaging \
    --no-ptex \
    --openvdb \
    --no-embree \
    --no-prman \
    --no-openimageio \
    --no-opencolorio \
    --alembic \
    --no-hdf5 \
    --draco \
    --materialx \
    "${OPENUSD_INSTALL_DIR}" && \
    rm -rf "${OPENUSD_SRC_DIR}" "${OPENUSD_INSTALL_DIR}/src"

### Copy Isaac Sim into the base image
ARG ISAAC_SIM_PATH="/root/isaac_sim"
ARG CARB_APP_PATH="${ISAAC_SIM_PATH}/kit"
ENV ISAAC_SIM_PYTHON_EXE="${ISAAC_SIM_PATH}/python.sh"
COPY --from=isaac_sim /isaac-sim "${ISAAC_SIM_PATH}"
COPY --from=isaac_sim /root/.nvidia-omniverse/config /root/.nvidia-omniverse/config
COPY --from=isaac_sim /etc/vulkan/icd.d/nvidia_icd.json /etc/vulkan/icd.d/nvidia_icd.json
RUN ISAAC_SIM_VERSION="$(cut -d'-' -f1 < "${ISAAC_SIM_PATH}/VERSION")" && \
    echo -e "\n# Isaac Sim ${ISAAC_SIM_VERSION}" >> /entrypoint.bash && \
    echo "export ISAAC_SIM_VERSION=\"${ISAAC_SIM_VERSION}\"" >> /entrypoint.bash && \
    echo "export ISAAC_SIM_PATH=\"${ISAAC_SIM_PATH}\"" >> /entrypoint.bash && \
    echo "export ISAACSIM_PATH=\"${ISAAC_SIM_PATH}\"" >> /entrypoint.bash && \
    echo "export ISAAC_SIM_PYTHON_EXE=\"${ISAAC_SIM_PYTHON_EXE}\"" >> /entrypoint.bash && \
    echo "export ISAACSIM_PYTHON_EXE=\"${ISAAC_SIM_PYTHON_EXE}\"" >> /entrypoint.bash && \
    echo "export CARB_APP_PATH=\"${CARB_APP_PATH}\"" >> /entrypoint.bash && \
    echo "export OMNI_SERVER=\"http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/${ISAAC_SIM_VERSION}\"" >> /entrypoint.bash && \
    echo "export OMNI_KIT_ALLOW_ROOT=\"1\"" >> /entrypoint.bash && \
    echo "# source \"${CARB_APP_PATH}/setup_python_env.sh\" --" >> /entrypoint.bash && \
    echo "# source \"${ISAAC_SIM_PATH}/setup_python_env.sh\" --" >> /entrypoint.bash

### Redownload Carbonite
#   Reason: Isaac Sim 2023.1.X Docker image seems to have some issues with symbolic links (or something) and it causes problems with linking OpenUSD libraries in Rust
ARG CARB_APP_REDOWNLOAD=true
ARG CARB_APP_REDOWNLOAD_VERSION="105.1.2"
ARG CARB_APP_REDOWNLOAD_BUILD_HASH="release.133510.b82c1e1e"
ARG CARB_APP_REDOWNLOAD_URL="https://d4i3qtqj3r0z5.cloudfront.net/kit-sdk%40${CARB_APP_REDOWNLOAD_VERSION}%2B${CARB_APP_REDOWNLOAD_BUILD_HASH}.tc.linux-x86_64.release.7z"
RUN if [[ "${CARB_APP_REDOWNLOAD,,}" = true ]]; then \
    echo -e "\n# Carb app ${CARB_APP_REDOWNLOAD_VERSION}" >> /entrypoint.bash && \
    echo "export CARB_APP_PATH=\"${CARB_APP_PATH}\"" >> /entrypoint.bash && \
    echo "# source \"${CARB_APP_PATH}/setup_python_env.sh\" --" >> /entrypoint.bash && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    ca-certificates \
    curl \
    p7zip-full && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf "${CARB_APP_PATH}" && \
    CARB_APP_DL_PATH="/tmp/kit-sdk-${CARB_APP_REDOWNLOAD_VERSION}+${CARB_APP_REDOWNLOAD_BUILD_HASH}.tc.linux-x86_64.release.7z" && \
    curl --proto "=https" --tlsv1.2 -sSfL "${CARB_APP_REDOWNLOAD_URL}" -o "${CARB_APP_DL_PATH}" && \
    7z x "${CARB_APP_DL_PATH}" -o"${CARB_APP_PATH}" && \
    rm "${CARB_APP_DL_PATH}" ; \
    fi

### Install additional dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    build-essential \
    clang \
    cmake \
    git \
    libarchive-dev \
    libgl-dev \
    libglu-dev \
    libilmbase-dev \
    libssl-dev \
    libx11-dev \
    libxt-dev \
    nvidia-cuda-dev \
    pkg-config \
    pybind11-dev \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

### (Optional) Install Blender Python module
ARG INSTALL_BPY=true
ARG BPY_VERSION="3.6.0"
RUN if [[ "${INSTALL_BPY,,}" = true ]]; then \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    libdbus-1-dev \
    libsm6 \
    libxcursor-dev \
    libxi-dev \
    libxinerama-dev \
    libxkbcommon-dev \
    libxrandr-dev \
    libxxf86vm-dev && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir bpy=="${BPY_VERSION}" ; \
    fi

### Install Rust
ARG RUST_VERSION="1.75"
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    ca-certificates \
    curl \
    mold && \
    rm -rf /var/lib/apt/lists/* && \
    curl --proto "=https" --tlsv1.2 -sSfL "https://sh.rustup.rs" | sh -s -- --no-modify-path -y --default-toolchain "${RUST_VERSION}" --profile default && \
    echo -e "\n# Rust ${RUST_VERSION}" >> /entrypoint.bash && \
    echo "source \"${HOME}/.cargo/env\" --" >> /entrypoint.bash && \
    echo "export CARGO_TARGET_DIR=\"${HOME}/ws_target\"" >> /entrypoint.bash && \
    echo "export CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_RUSTFLAGS=\"-Clink-arg=-fuse-ld=mold -Ctarget-cpu=native\"" >> /entrypoint.bash

### Install RL dependencies
# NOTE: Python packages for which Rust bindings are generated via pyo3_bindgen are installed both for Isaac and system (shouldn't be necessary, but avoids some issues)
RUN $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir setuptools==65.5.0 && \
    $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir gymnasium==0.29.1 && \
    $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir stable-baselines3[extra]==2.2.1 sb3-contrib==2.2.1 && \
    $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir git+https://github.com/AndrejOrsula/dreamerv3.git@no_replay_saver && \
    $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir --upgrade "jax[cuda11_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    python3 -m pip install --no-cache-dir setuptools==65.5.0 && \
    python3 -m pip install --no-cache-dir gymnasium==0.29.1 && \
    python3 -m pip install --no-cache-dir stable-baselines3[extra]==2.2.1 sb3-contrib==2.2.1 && \
    python3 -m pip install --no-cache-dir git+https://github.com/AndrejOrsula/dreamerv3.git@no_replay_saver && \
    python3 -m pip install --no-cache-dir --upgrade "jax[cuda11_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

### Use Python embedded inside Isaac Sim
RUN echo "export PYO3_PYTHON=\"${ISAAC_SIM_PYTHON_EXE}\"" >> /entrypoint.bash

### Finalize the entrypoint and source it in the ~/.bashrc
# hadolint ignore=SC2016
RUN echo -e "\n# Execute the command" >> /entrypoint.bash && \
    echo -en 'exec "${@}"\n' >> /entrypoint.bash && \
    echo -e "\n# Source the entrypoint" >> "${HOME}/.bashrc" && \
    echo -en "source /entrypoint.bash --\n" >> "${HOME}/.bashrc"
ENTRYPOINT ["/entrypoint.bash"]

### Configure the workspace
ARG WORKSPACE="/root/ws"
ENV WORKSPACE="${WORKSPACE}"
WORKDIR ${WORKSPACE}

### Copy the source
COPY . "${WORKSPACE}"

# RUN $ISAAC_SIM_PYTHON_EXE -m pip uninstall -y typing_extensions && $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir typing_extensions==4.10.0 && $ISAAC_SIM_PYTHON_EXE -m pip install --no-cache-dir matplotlib

### Build the workspace
RUN source /entrypoint.bash -- && \
    cargo build --release --all-targets

### Generate training set
RUN source /entrypoint.bash -- && \
    cargo run --release --bin generate_peg_in_hole_train

### Singularity: Create directories that will mounted
RUN mkdir -p "${ISAAC_SIM_PATH}/kit/cache" && \
    mkdir -p "/root/.cache/nvidia/GLCache" && \
    mkdir -p "/root/.cache/ov" && \
    mkdir -p "/root/.cache/pip" && \
    mkdir -p "/root/.local/share/ov/data" && \
    mkdir -p "/root/.nv/ComputeCache" && \
    mkdir -p "/root/.nvidia-omniverse/logs" && \
    mkdir -p "/root/Documents"

### Set the default command
CMD ["bash"]
