import gymnasium as gym
env = gym.make('Assault-v0', render_mode="human")
observation = env.reset()
# stan i zestaw akcji dyskretne
for _ in range(300):
    action = env.action_space.sample()
    observation = env.step(action)
