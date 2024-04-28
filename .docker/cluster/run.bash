#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
REPOSITORY_DIR="$(dirname "$(dirname "${SCRIPT_DIR}")")"
REPOSITORY_NAME="$(basename "${REPOSITORY_DIR}")"

## Configuration
# Path to the image
IMAGE_PATH="${IMAGE_PATH:-"${SCRATCH:-${HOME}}/images/${REPOSITORY_NAME}.sif"}"
# Flags for running the container
SINGULARITY_EXEC_OPTS="${SINGULARITY_EXEC_OPTS:-
    --no-home
}"
# Flags for enabling GPU inside the container
ENABLE_GPU="${ENABLE_GPU:-true}"
# List of volumes to mount (can be updated by passing -v HOST_DIR:DOCKER_DIR:OPTIONS)
CACHE_ROOT="${SCRATCH:-${HOME}}/cache/${REPOSITORY_NAME}"
CUSTOM_VOLUMES=(
    # Omniverse / Isaac Sim
    "${CACHE_ROOT}/cache/computecache:/root/.nv/ComputeCache:rw"
    "${CACHE_ROOT}/cache/exts/omni.gpu_foundation:/root/isaac_sim/kit/exts/omni.gpu_foundation/cache:rw"
    "${CACHE_ROOT}/cache/glcache:/root/.cache/nvidia/GLCache:rw"
    "${CACHE_ROOT}/cache/kit:/root/isaac_sim/kit/cache:rw"
    "${CACHE_ROOT}/cache/ov:/root/.cache/ov:rw"
    "${CACHE_ROOT}/cache/pip:/root/.cache/pip:rw"
    "${CACHE_ROOT}/data/kit:/root/isaac_sim/kit/data:rw"
    "${CACHE_ROOT}/data/ov:/root/.local/share/ov/data:rw"
    "${CACHE_ROOT}/documents:/root/Documents:rw"
    "${CACHE_ROOT}/home/users:/home/users:rw"
    "${CACHE_ROOT}/logs:/root/.nvidia-omniverse/logs:rw"
    # Workspace
    "${REPOSITORY_DIR}:/root/ws:rw"
    # Logs
    "${SCRATCH:-${HOME}}/logs/${REPOSITORY_NAME}:/logs:rw"
)

## Ensure the image exists
if [ ! -f "${IMAGE_PATH}" ]; then
    echo >&2 -e "\033[1;31mERROR: Singularity image not found at ${IMAGE_PATH}\033[0m"
    exit 1
fi

## Parse CMD
if [ "${#}" -gt "0" ]; then
    CMD=${*:1}
else
    echo >&2 -e "\033[1;31mERROR: No command provided.\033[0m"
    exit 1
fi

## Ensure the host directories exist
for volume in "${CUSTOM_VOLUMES[@]}"; do
    if [[ "${volume}" =~ ^([^:]+):([^:]+).*$ ]]; then
        host_dir="${BASH_REMATCH[1]}"
        if [ ! -d "${host_dir}" ]; then
            mkdir -p "${host_dir}"
            echo -e "\033[1;90mINFO: Created directory ${host_dir}\033[0m"
        fi
    fi
done

## GPU
if [[ "${ENABLE_GPU,,}" = true ]]; then
    GPU_OPT="--nv"
fi

## Environment
if ! command -v module >/dev/null 2>&1; then
    echo >&2 -e "\033[1;31mERROR: The 'module' command is not available. Please run this script on a compute node.\033[0m"
    exit 1
fi
# Load the Singularity module
module purge
module load tools/Singularity

## Run the container
# shellcheck disable=SC2206
SINGULARITY_EXEC_CMD=(
    ${SINGULARITY_EXEC_CMD_PREFIX} singularity exec
    "${SINGULARITY_EXEC_OPTS}"
    "${GPU_OPT}"
    "${CUSTOM_VOLUMES[@]/#/"--bind "}"
    "${IMAGE_PATH}"
    "${CMD}"
)
echo -e "\033[1;90m${SINGULARITY_EXEC_CMD[*]}\033[0m" | xargs
# shellcheck disable=SC2048
exec ${SINGULARITY_EXEC_CMD[*]}
