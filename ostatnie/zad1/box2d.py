import gymnasium as gym
env = gym.make("BipedalWalker-v3", hardcore=True, render_mode="human")
observation = env.reset()
# stan i zestaw akcji ciągłe (w przypadku tej gry)
for _ in range(300):
    action = env.action_space.sample()
    observation = env.step(action)