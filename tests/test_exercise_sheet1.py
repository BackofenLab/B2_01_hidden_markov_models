from __future__ import division
from math import isclose, prod
import pytest
from random import seed, uniform, randint, shuffle, choices
from helpers.helpers import *
from exercise_sheet1 import *

seed(10)

N_TESTS = 10
LOAD_PROBABILITIES = [1 / 10, 1 / 10, 1 / 10, 2 / 10, 2 / 10, 3 / 10]


def test_exercise_3a():
    """
    For details check README.
    """
    for i in range(N_TESTS):
        shuffle(LOAD_PROBABILITIES)
        fair_die = Die(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)
        loaded_die = Die(*LOAD_PROBABILITIES)
        probability_loaded = uniform(0.1, 0.9)
        probability_fair = 1 - probability_loaded
        casino_dice = [(fair_die, probability_fair), (loaded_die, probability_loaded)]
        roll = randint(1, 6)
        response = roll_proba_given_dice(casino_dice, roll)
        solution = roll_proba_given_dice_correct(casino_dice, roll)
        if response is None:
            print("[x] It seems that you haven't implemented the function!")
            break
        if solution != response:
            print("[x] It seems that your implementation is wrong.")
            print("\t[o] Probability fair: {}".format(probability_fair))
            print("\t[o] Probability loaded: {}".format(probability_loaded))
            print("\t[o] Roll: {}".format(roll))
            print("\t\t[-] Your result: {}".format(response))
            print("\t\t[+] Correct value: {}".format(solution))
        assert response == solution


def test_exercise_3b():
    """
    For details check README.
    """
    for i in range(N_TESTS):
        shuffle(LOAD_PROBABILITIES)
        die = Die(*LOAD_PROBABILITIES)
        observation = [randint(1, 6) for x in range(randint(1, 20))]
        response = observation_given_die(die, observation)
        solution = observation_given_die_correct(die, observation)
        if response is None:
            print("[x] It seems that you haven't implemented the function!")
            break
        if solution != response:
            print("[x] It seems that your implementation is wrong.")
            print("\t[o] Die probabilities: {}".format(LOAD_PROBABILITIES))
            print("\t[o] Observation: {}".format(observation))
            print("\t\t[-] Your result: {}".format(response))
            print("\t\t[+] Correct value: {}".format(solution))
        assert response == solution


def test_exercise_3c():
    """
    For details check README.
    """
    for i in range(N_TESTS):
        shuffle(LOAD_PROBABILITIES)
        fair_die = Die(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)
        loaded_die = Die(*LOAD_PROBABILITIES)
        probability_loaded = uniform(0.1, 0.9)
        probability_fair = 1 - probability_loaded
        casino_dice = [(fair_die, probability_fair), (loaded_die, probability_loaded)]
        observation = [randint(1, 6) for x in range(randint(1, 20))]
        response = proba_of_dice_given_observation(casino_dice, observation)
        solution = proba_of_dice_given_observation_correct(casino_dice, observation)
        if response is None:
            print("[x] It seems that you haven't implemented the function!")
            break
        if solution != response:
            print("[x] It seems that your implementation is wrong.")
            print("\t[o] Loaded die probabilities: {}".format(LOAD_PROBABILITIES))
            print("\t[o] Probability picking loaded die: {}".format(probability_loaded))
            print("\t[o] Observation: {}".format(observation))
            print("\t\t[-] Your result: {}".format(response))
            print("\t\t[+] Correct value: {}".format(solution))
        assert response == solution


def test_exercise_3d():
    """
    For details check README.
    """
    for i in range(N_TESTS):
        shuffle(LOAD_PROBABILITIES)
        fair_die = Die(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)
        loaded_die = Die(*LOAD_PROBABILITIES)
        probability_loaded = uniform(0.1, 0.9)
        probability_fair = 1 - probability_loaded
        casino_dice = [(fair_die, probability_fair), (loaded_die, probability_loaded)]
        t1, t2 = uniform(0.1, 0.9), uniform(0.1, 0.9)
        transition = [(t1, 1 - t1), (t2, 1 - t2)]
        state_sequence = "".join(choices(["0", "1"], k=randint(2, 10)))
        response = state_sequence_probability_computation(
            casino_dice, state_sequence, transition
        )
        solution = state_sequence_probability_computation_correct(
            casino_dice, state_sequence, transition
        )
        if response is None:
            print("[x] It seems that you haven't implemented the function!")
            break
        if solution != response:
            print("[x] It seems that your implementation is wrong.")
            print("\t[o] Loaded die probabilities: {}".format(LOAD_PROBABILITIES))
            print("\t[o] Probability picking loaded die: {}".format(probability_loaded))
            print("\t[o] Transition matrix: {}".format(transition))
            print("\t[o] State sequence: {}".format(state_sequence))
            print("\t\t[-] Your result: {}".format(response))
            print("\t\t[+] Correct value: {}".format(solution))
        assert response == solution


def test_exercise_3e():
    """
    For details check README.
    """
    for i in range(N_TESTS):
        shuffle(LOAD_PROBABILITIES)
        fair_die = Die(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)
        loaded_die = Die(*LOAD_PROBABILITIES)
        probability_loaded = uniform(0.1, 0.9)
        probability_fair = 1 - probability_loaded
        casino_dice = [(fair_die, probability_fair), (loaded_die, probability_loaded)]
        observation = [randint(1, 6) for x in range(randint(1, 20))]
        state_sequence = "".join(choices(["0", "1"], k=randint(2, 10)))
        response = observation_probability_computation_given_state_sequence(
            casino_dice, observation, state_sequence
        )
        solution = observation_probability_computation_given_state_sequence_correct(
            casino_dice, observation, state_sequence
        )
        if response is None:
            print("[x] It seems that you haven't implemented the function!")
            break
        if solution != response:
            print("[x] It seems that your implementation is wrong.")
            print("\t[o] Loaded die probabilities: {}".format(LOAD_PROBABILITIES))
            print("\t[o] Probability picking loaded die: {}".format(probability_loaded))
            print("\t[o] Observation: {}".format(observation))
            print("\t[o] State sequence: {}".format(state_sequence))
            print("\t\t[-] Your result: {}".format(response))
            print("\t\t[+] Correct value: {}".format(solution))
        assert response == solution


def test_exercise_3f():
    """
    For details check README.
    """
    for i in range(N_TESTS):
        shuffle(LOAD_PROBABILITIES)
        fair_die = Die(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)
        loaded_die = Die(*LOAD_PROBABILITIES)
        probability_loaded = uniform(0.1, 0.9)
        probability_fair = 1 - probability_loaded
        casino_dice = [(fair_die, probability_fair), (loaded_die, probability_loaded)]
        observation = [randint(1, 6) for x in range(randint(1, 20))]
        state_sequence = "".join(choices(["0", "1"], k=randint(2, 10)))
        t1, t2 = uniform(0.1, 0.9), uniform(0.1, 0.9)
        transition = [(t1, 1 - t1), (t2, 1 - t2)]

        response = observation_state_sequence_joint_probability_computation(
            casino_dice, observation, state_sequence, transition
        )
        solution = observation_state_sequence_joint_probability_computation_correct(
            casino_dice, observation, state_sequence, transition
        )
        if response is None:
            print("[x] It seems that you haven't implemented the function!")
            break
        if solution != response:
            print("[x] It seems that your implementation is wrong.")
            print("\t[o] Loaded die probabilities: {}".format(LOAD_PROBABILITIES))
            print("\t[o] Probability picking loaded die: {}".format(probability_loaded))
            print("\t[o] Observation: {}".format(observation))
            print("\t[o] State sequence: {}".format(state_sequence))
            print("\t\t[-] Your result: {}".format(response))
            print("\t\t[+] Correct value: {}".format(solution))
        assert response == solution
