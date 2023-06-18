import gym
import numpy as np

env = gym.make('FrozenLake8x8-v1', render_mode="human")

# Stan gry i zestaw akcji są dyskretne


import random
import time

# random array of size 1000 , 0 - 3
valid_actions = np.random.randint(0, 4, size=1000)
maximal_accepted_excess_distance = 0

def observation_to_position(observation): # 0, 1, 2, 3, 4, 5, 6, 7, 8
    ncols = 8
    current_row = observation // ncols
    current_col = observation % ncols
    return current_row, current_col
import math


def calculate_distance(pos1, pos2): # params (x1, y1), (x2, y2)
    # return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def decide_action(observation, step_number, valid_actions): # 0, 1, 2, 3
    # print("Stan gry: ", observation)
    # The observation is a value representing
    # the player’s current position
    # as current_row * nrows + current_col
    # (where both the row and col start at 0).

    # return random.randint(0, 3)
    return valid_actions[step_number]

while True:
    observation, info = env.reset(seed=42)
    current_distance = calculate_distance(observation_to_position(observation), (7, 7))
    print("Rozpoczynamy nową grę")
    for step_number in range(1000):
        # time.sleep(0.5)
        action = decide_action(observation, step_number, valid_actions)

        action_jako_text = {0: 'lewo', 1: 'dół', 2: 'prawo', 3: 'góra'}[action]
        print(f"Podjęto akcję: {action_jako_text}")
        new_observation, reward, terminated, truncated, info = env.step(action)
        new_distance = calculate_distance(observation_to_position(new_observation), (7, 7))
        print("stara odległość: ", current_distance, " nowa odległość: ", new_distance)
        if terminated or truncated:
            maximal_accepted_excess_distance += 0.5
            print(f"Mogę się teraz oddalać nawet o {maximal_accepted_excess_distance}")
            old_bad_action = valid_actions[step_number]
            new_action = random.randint(0, 3)
            while new_action == old_bad_action:
                new_action = random.randint(0, 3)
            valid_actions[step_number] = new_action
            print("Koniec gry")
            break
        elif new_distance > current_distance + maximal_accepted_excess_distance:
            old_bad_action = valid_actions[step_number]
            new_action = random.randint(0, 3)
            while new_action == old_bad_action:
                new_action = random.randint(0, 3)
            valid_actions[step_number] = new_action
            print("Złe działanie, zabijam i poprawiam")
            break
        observation = new_observation
        current_distance = new_distance
   #  break
   #  time.sleep(2)
