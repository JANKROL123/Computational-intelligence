import math
import random
import time

import gym
import numpy as np
import pygad

env = gym.make('FrozenLake8x8-v1', is_slippery=False)

def decide_action(solution, observation, step_number):
    return int(solution[step_number])

def observation_to_position(observation): # 0, 1, 2, 3, 4, 5, 6, 7, 8
    ncols = 8
    current_row = observation // ncols
    current_col = observation % ncols
    return current_row, current_col


def calculate_distance(pos1, pos2): 
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)


def simulate(env, solution, decide_action):
    current_observation, info = env.reset()
    current_distance = calculate_distance(observation_to_position(current_observation), (7, 7))
    for step_number in range(200):
        action = decide_action(solution, current_observation, step_number)
        new_observation, reward, terminated, truncated, info = env.step(action)
        new_distance = calculate_distance(observation_to_position(new_observation), (7, 7))
        # truncated - koniec czasu, ta gra ma 200 kroków domyślnie
        # terminated - koniec gry, wpadliśmy do dziury lub do celu
        current_observation = new_observation
        current_distance = new_distance
        if truncated or terminated:
            break
    total_reward = -current_distance - 0.1 * step_number
    return total_reward

def generate_fitness_func(env, decide_action):
    def fitness_func(ga_instance, solution, solution_idx):
        return simulate(env, solution, decide_action)
    return fitness_func

fitness_func = generate_fitness_func(env, decide_action)

def on_generation(ga_instance):
    print(f"{ga_instance.generations_completed} {ga_instance.best_solution()[1]}")


ga_instance = pygad.GA(
        gene_space=[0, 1, 2, 3],
        num_generations=300,
        fitness_func=fitness_func,
        sol_per_pop=20,
        num_genes=200,
        num_parents_mating=10,
        parent_selection_type="sss",
        crossover_type="single_point",
        keep_parents=3,
        mutation_type="random",
        mutation_probability=0.1,
        on_generation=on_generation,
    )
        
ga_instance.run()

best_solution, best_solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Best solution: {best_solution}")
print(f"Best solution fitness: {best_solution_fitness}")
print(f"Wizualizacja:")
env = gym.make('FrozenLake8x8-v1', is_slippery=False, render_mode='human')
simulate(env, best_solution, decide_action)