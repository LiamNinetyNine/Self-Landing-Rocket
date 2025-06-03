import gymnasium as gym


class Environment:
    def __init__(self, environment_type):
        self.environment_type = environment_type

    def init_env(self):
        # Initialise the environment
        env = gym.make(self.environment_type, render_mode="human")
        # Reset the environment to generate the first observation
        observation, info = env.reset(seed=42)
        for _ in range(1000):
            # this is where you would insert your policy
            action = env.action_space.sample()
            # step (transition) through the environment with the action
            # receiving the next observation, reward and if the episode has terminated or truncated
            observation, reward, terminated, truncated, info = env.step(action)
            # If the episode has ended then we can reset to start a new episode
            if terminated or truncated:
                observation, info = env.reset()
        env.close()

if __name__ == "__main__":
    env = Environment("LunarLander-v3")
    env.init_env()