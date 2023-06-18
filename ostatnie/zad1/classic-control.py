import time

import gymnasium as gym

env = gym.make('CartPole-v1', render_mode="human")
# stan ciągły i zestaw akcji dyskretny

def decide_action(observation):
    pole_angle = observation[2]
    if pole_angle < 0:
        return 0 
    else:
        return 1 

while True:
    observation, _ = env.reset()
    print("Rozpoczynamy nową grę")
    for _ in range(1000):
        time.sleep(0.5)
        action = decide_action(observation)
        print(f"Podjęto akcję: {action}")
        new_observation, reward, terminated, truncated, info = env.step(action)
        observation = new_observation
        if terminated or truncated:
            print("Koniec gry")
            break
        print("Nagroda: ", reward)
    break
    time.sleep(2)


