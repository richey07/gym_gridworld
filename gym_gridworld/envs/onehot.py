"""
Gym implementation of small grid world, where states are represented
as one-hot encodings
"""
import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
from gym_gridworld.envs.gridworld import GridWorldEnv

class OneHotGridWorldEnv(GridWorldEnv):
	metadata = {'render.modes': ['human']}

	def get_state(self):
		"""
		takes the position of the 1 (self.state) and turns this
		into a one-hot encoding representation of the current state
		"""
		row, col = self.state
		state_vec = np.zeros(self.size**2)
		idx = self.size*row + col
		state_vec[idx] = 1
		return state_vec

	#length of a one-hot vector
	def state_size(self):
		return self.size ** 2