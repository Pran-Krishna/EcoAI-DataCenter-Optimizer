import gymnasium as gym
from gymnasium import spaces
import numpy as np

# Standard Gymnasium Environment (OpenEnv compatible)
class EcoServerManager(gym.Env):
    def __init__(self, task_id="low_load_day"):
        super().__init__()
        self.task_id = task_id
        # 0: Low, 1: Normal, 2: Turbo
        self.action_space = spaces.Discrete(3) 
        # [Load, Carbon, Price, Temp]
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        if self.task_id == "emergency_overheat":
            self.state = np.array([0.5, 0.5, 0.5, 0.9], dtype=np.float32)
        elif self.task_id == "high_carbon_peak":
            self.state = np.array([0.4, 0.9, 0.8, 0.4], dtype=np.float32)
        else:
            self.state = np.random.rand(4).astype(np.float32)
        return self.state, {}

    def step(self, action):
        load, carbon, price, temp = self.state
        reward = 0.5 
        
        # Reward Logic (0.0 to 1.0 range as per screenshot)
        if carbon > 0.7 and action == 0: reward += 0.2
        if temp > 0.8 and action == 2: reward -= 0.4
        if load > 0.8 and action == 2: reward += 0.3
        
        reward = float(np.clip(reward, 0.0, 1.0))
        self.state = np.random.rand(4).astype(np.float32)
        
        # OpenEnv expects: obs, reward, terminated, truncated, info
        return self.state, reward, True, False, {"score": reward}
