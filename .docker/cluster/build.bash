#!/usr/bin/env bash
set -e

## Configuration
# Default Docker Hub user (used if user is not logged in)
DEFAULT_DOCKERHUB_USER="andrejorsula"

## Determine the name of the image to run (automatically inferred from the current user and repository, or using the default if not available)
# Get the current Docker Hub user or use the default
DOCKERHUB_USER="$(${WITH_SUDO} docker info | sed '/Username:/!d;s/.* //')"
DOCKERHUB_USER="${DOCKERHUB_USER:-${DEFAULT_DOCKERHUB_USER}}"
# Get the name of the repository (directory)
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
DOT_DOCKER_DIR="$(dirname "${SCRIPT_DIR}")"
REPOSITORY_DIR="$(dirname "$(dirname "${SCRIPT_DIR}")")"
if [[ -f "${REPOSITORY_DIR}/Dockerfile" ]]; then
    REPOSITORY_NAME="$(basename "${REPOSITORY_DIR}")"
else
    echo >&2 -e "\033[1;31mERROR: Cannot build Docker image because \"${REPOSITORY_DIR}/Dockerfile\" does not exist.\033[0m"
    exit 1
fi
# Combine the user and repository name to form the image name
DOCKER_IMAGE_NAME="${DOCKERHUB_USER}/${REPOSITORY_NAME}"

## Parse TAG
if [ "${#}" -gt "0" ]; then
    if [[ "${1}" != "-"* ]]; then
        DOCKER_IMAGE_NAME="${DOCKER_IMAGE_NAME}:${1}"
    else
        DOCKER_IMAGE_NAME="${DOCKER_IMAGE_NAME}:latest"
    fi
else
    DOCKER_IMAGE_NAME="${DOCKER_IMAGE_NAME}:latest"
fi

## Determine the name of the Singularity image
APPTAINER_IMAGE_NAME="${REPOSITORY_NAME}"
APPTAINER_IMAGE_PATH="${SCRIPT_DIR}/${APPTAINER_IMAGE_NAME}.sif"

## If the file already exists, ask the user if it should be overwritten
if [ -f "${APPTAINER_IMAGE_PATH}" ]; then
    read -p "[INFO] The file \"${APPTAINER_IMAGE_PATH}\" already exists. Would you like to overwrite it? (y/N)" app_answer
    if [ "$app_answer" != "${app_answer#[Yy]}" ]; then
        # rm -f "${APPTAINER_IMAGE_PATH}"
        echo "[INFO] Continuing..."
    else
        echo "[INFO] Exiting because the file already exists"
        exit
    fi
fi

## Ensure the Docker image is built
DOCKER_BUILD_SCRIPT_PATH="${DOT_DOCKER_DIR}/build.bash"
"${DOCKER_BUILD_SCRIPT_PATH}"

## Convert the Docker image to a Singularity image
apptainer build "${APPTAINER_IMAGE_PATH}" "docker-daemon://${DOCKER_IMAGE_NAME}"
