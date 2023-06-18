import math
import random
import time

import gym
import numpy as np
import pygad
from simpful import *


FS = FuzzySystem()

FS.add_linguistic_variable(
    "angle",
    LinguisticVariable(
        [
            FuzzySet(function=Triangular_MF(-math.pi, -math.pi/2, 0), term="left"),
            FuzzySet(function=Triangular_MF(-math.pi/2, 0, math.pi/2), term="center"),
            FuzzySet(function=Triangular_MF(0, math.pi/2, math.pi), term="right"),
		],
        universe_of_discourse=[-math.pi,math.pi]
    )
)
FS.add_linguistic_variable(
    "angular_velocity",
    LinguisticVariable(
        [
            FuzzySet(function=Triangular_MF(-8, -8, 0), term="left"),
            FuzzySet(function=Triangular_MF(-8, -8, -4), term="left_fast"),
            FuzzySet(function=Triangular_MF(-8, -4, 0), term="left_slow"),
            FuzzySet(function=Triangular_MF(-4, 0, 4), term="center"),
            FuzzySet(function=Triangular_MF(0, 4, 8), term="right_slow"),
            FuzzySet(function=Triangular_MF(4, 8, 8), term="right_fast"),
            FuzzySet(function=Triangular_MF(0, 8, 8), term="right"),
		],
        universe_of_discourse=[-8,8]
	)
)
FS.add_linguistic_variable(
    "torque",
    LinguisticVariable(
		[
			FuzzySet(function=Triangular_MF(-2, -2, 0), term="left"),
			FuzzySet(function=Triangular_MF(-2, -2, -1), term="left_fast"),
			FuzzySet(function=Triangular_MF(-2, -1, 0), term="left_slow"),
			FuzzySet(function=Triangular_MF(-1, 0, 1), term="off"),
			FuzzySet(function=Triangular_MF(0, 1, 2), term="right_slow"),
			FuzzySet(function=Triangular_MF(1, 2, 2), term="right_fast"),
			FuzzySet(function=Triangular_MF(0, 2, 2), term="right"),
		],
		universe_of_discourse=[-2,2]
	)
)

FS.add_rules([
	"IF (angle IS left) AND (angular_velocity IS left) THEN (torque IS left)",
    "IF (angle IS left) AND (angular_velocity IS right) THEN (torque IS right)",
    "IF (angle IS right) AND (angular_velocity IS left) THEN (torque IS left)",
    "IF (angle IS right) AND (angular_velocity IS right) THEN (torque IS right)",
    "IF (angle IS center) AND (angular_velocity IS left) THEN (torque IS left)",
    "IF (angle IS center) AND (angular_velocity IS right) THEN (torque IS right)",
	"IF (angle IS left) AND (angular_velocity IS center) THEN (torque IS off)",
    "IF (angle IS left) AND (angular_velocity IS center) THEN (torque IS off)",
    "IF (angle IS right) AND (angular_velocity IS center) THEN (torque IS off)",
    "IF (angle IS right) AND (angular_velocity IS center) THEN (torque IS off)",   
])

def decide_action(observation):
    angle = (math.atan2(observation[1], observation[0]) % ( 2 * math.pi)) - math.pi
    angular_velocity = observation[2]
    FS.set_variable("angle", angle)
    FS.set_variable("angular_velocity", angular_velocity)
    torque = FS.inference()["torque"]
    
    return (torque,)

def simulate(env, decide_action):
    current_observation, info = env.reset()
    total_reward = 0.0
    while True:
        time.sleep(0.2)
        action = decide_action(current_observation)
        new_observation, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        # truncated - koniec czasu, ta gra ma 200 kroków domyślnie
        # terminated - koniec gry, wpadliśmy do dziury lub do celu
        current_observation = new_observation
        if truncated or terminated:
            break
    return total_reward


env = gym.make('Pendulum-v1', g=9.81, render_mode='human')


result = simulate(env, decide_action)
print(result)
