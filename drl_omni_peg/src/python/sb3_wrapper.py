from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple, TypeVar, Union

import gymnasium
import numpy as np
from stable_baselines3.common.vec_env.base_vec_env import VecEnv

U = TypeVar("U")
V = TypeVar("V")


class SingleProcessVecEnv(VecEnv):
    def __init__(self, env: Union[str, gymnasium.Env[U, V]], **kwargs):
        if isinstance(env, str):
            self._env: gymnasium.Env[U, V] = gymnasium.make(
                env, render_mode="rgb_array", **kwargs
            )
        else:
            self._env = env
        VecEnv.__init__(
            self, self.n_envs, self._env.observation_space, self._env.action_space
        )

        self._done = np.array([True for _ in range(self.n_envs)])

    @property
    def n_envs(self):
        return self._env.n_envs

    """
    Operations - MDP
    """

    def seed(self, seed: int | None = None) -> list[int | None]:
        return [seed] * self.unwrapped.num_envs

    def reset(self) -> Union[np.ndarray, Dict[str, np.ndarray], Tuple[np.ndarray, ...]]:
        reset_ret = self._env.reset()
        reset_observations = np.stack([obs for obs, _ in reset_ret])
        return reset_observations

    def step_async(self, actions):
        self._async_actions = actions

    def step_wait(self, actions=None) -> Tuple[
        Union[np.ndarray, Dict[str, np.ndarray], Tuple[np.ndarray, ...]],
        np.ndarray,
        np.ndarray,
        List[Dict],
    ]:
        if actions is None:
            actions = self._async_actions

        envs_to_reset = np.where(self._done == True)[0]
        envs_to_step = np.where(self._done == False)[0]

        if len(envs_to_reset) > 0:
            reset_ret = self._env.reset_envs(envs_to_reset)

            reset_observations = [obs for obs, _ in reset_ret]
            reset_info = [info for _, info in reset_ret]

            self._done[envs_to_reset] = False

        if len(envs_to_step) > 0:
            step_ret = self._env.step_envs(actions, envs_to_step)

            step_observations = [obs for obs, _, _, _, _ in step_ret]
            step_rewards = [reward for _, reward, _, _, _ in step_ret]
            step_terminated = [terminated for _, _, terminated, _, _ in step_ret]
            step_truncated = [truncated for _, _, _, truncated, _ in step_ret]
            step_info = [info for _, _, _, _, info in step_ret]

            self._done[envs_to_step] = np.logical_or(step_terminated, step_truncated)

        obs = []
        reward = []
        infos = []
        index_reset = 0
        index_step = 0
        for i in range(self.n_envs):
            if i in envs_to_reset:
                obs.append(reset_observations[index_reset])
                reward.append(0.0)
                infos.append(reset_info[index_reset])
                index_reset += 1
            else:
                obs.append(step_observations[index_step])
                reward.append(step_rewards[index_step])
                infos.append(step_info[index_step])
                index_step += 1

        obs = np.stack(obs)
        reward = np.stack(reward)

        return obs, reward, self._done, infos

    def close(self):
        self._env.close()

    def get_attr(self, attr_name, indices=None):
        if indices is None:
            indices = range(self.num_envs)
        num_indices = len(indices)
        attr_val = getattr(self._env, attr_name)
        if isinstance(attr_val, np.ndarray):
            return attr_val[indices].numpy()
        else:
            return [attr_val] * num_indices

    def set_attr(self, attr_name, value, indices=None):
        raise NotImplementedError()

    def env_method(
        self,
        method_name: str,
        *method_args,
        indices: Union[None, int, Iterable[int]] = None,
        **method_kwargs,
    ) -> List[Any]:
        env_method = getattr(self._env, method_name)
        return env_method(*method_args, indices=indices, **method_kwargs)

    def env_is_wrapped(self, wrapper_class, indices=None):
        return [False for _ in range(self.num_envs)]

    def step(self, actions: np.ndarray) -> Tuple[
        Union[np.ndarray, Dict[str, np.ndarray], Tuple[np.ndarray, ...]],
        np.ndarray,
        np.ndarray,
        List[Dict],
    ]:
        return self.step_wait(actions)

    def get_images(self):
        raise NotImplementedError()
