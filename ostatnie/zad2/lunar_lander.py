import math
import random
import time

import gym
import numpy as np
import pygad

env = gym.make('LunarLander-v2')

def decide_action(solution, observation, step_number):
    return int(solution[step_number])

def simulate(env, solution, decide_action):
    current_observation, info = env.reset()
    total_reward = 0.0
    for step_number in range(200):
        action = decide_action(solution, current_observation, step_number)
        new_observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        # truncated - koniec czasu, ta gra ma 200 kroków domyślnie
        # terminated - koniec gry, wpadliśmy do dziury lub do celu
        current_observation = new_observation
        if truncated or terminated:
            break
    return total_reward

def generate_fitness_func(env, decide_action):
    def fitness_func(ga_instance, solution, solution_idx):
        return simulate(env, solution, decide_action)
    return fitness_func

fitness_func = generate_fitness_func(env, decide_action)

def on_generation(ga_instance):
    print(f"{ga_instance.generations_completed} {ga_instance.best_solution()[1]}")
    if ga_instance.generations_completed % 10 == 0:
        env = gym.make('LunarLander-v2', render_mode='human')
        simulate(env, ga_instance.best_solution()[0], decide_action)


ga_instance = pygad.GA(
    gene_space=[0, 1, 2, 3],
    num_generations=100,
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
env = gym.make('LunarLander-v2', render_mode='human')
simulate(env, best_solution, decide_action)