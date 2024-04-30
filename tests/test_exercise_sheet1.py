from __future__ import division
from math import isclose, prod
import pytest
from random import seed, uniform, randint, shuffle, choices
from implementation import (Die, 
                            roll_proba_given_dice_correct, 
                            observation_given_die_correct, 
                            proba_of_dice_given_observation_correct,
                            state_sequence_probability_computation_correct,
                            observation_probability_computation_given_state_sequence_correct, 
                            observation_state_sequence_joint_probability_computation_correct)
                            
from exercise_sheet1 import  (roll_proba_given_dice, 
                              observation_given_die, 
                              proba_of_dice_given_observation,
                              state_sequence_probability_computation,
                              observation_probability_computation_given_state_sequence, 
                              observation_state_sequence_joint_probability_computation)


dice_data = [
    [(Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6), 0.8), (Die(0.1, 0.1, 0.1, 0.1, 0.1, 0.5), 0.2)],
]

roll_values = [1, 2, 3, 4, 5, 6]

observations = [
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1],
]

state_sequences = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
]

transition_matrix = [
    [0.99, 0.01],
    [0.03, 0.97],
]

# Tests

@pytest.mark.parametrize("list_dice,roll_value", [(d, rv) for d in dice_data for rv in roll_values])
def test_roll_proba_given_dice_3a(list_dice, roll_value):
    expected = roll_proba_given_dice_correct(list_dice, roll_value)
    result = roll_proba_given_dice(list_dice, roll_value)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("die,observation", [(d[0][0], obs) for d in dice_data for obs in observations])
def test_observation_given_die_3b(die, observation):
    expected = observation_given_die_correct(die, observation)
    result = observation_given_die(die, observation)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("list_dice,observation", [(d, obs) for d in dice_data for obs in observations])
def test_proba_of_dice_given_observation_3c(list_dice, observation):
    expected = proba_of_dice_given_observation_correct(list_dice, observation)
    result = proba_of_dice_given_observation(list_dice, observation)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("list_dice,state_sequence,transition_matrix", [(d, ss, transition_matrix) for d in dice_data for ss in state_sequences])
def test_state_sequence_probability_computation_3d(list_dice, state_sequence, transition_matrix):
    expected = state_sequence_probability_computation_correct(list_dice, state_sequence, transition_matrix)
    result = state_sequence_probability_computation(list_dice, state_sequence, transition_matrix)
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.parametrize("list_dice,observation,state_sequence", [(d, obs, ss) for d in dice_data for obs in observations for ss in state_sequences])
def test_observation_probability_computation_given_state_sequence_3e(list_dice, observation, state_sequence):
    expected = observation_probability_computation_given_state_sequence_correct(list_dice, observation, state_sequence)
    result = observation_probability_computation_given_state_sequence(list_dice, observation, state_sequence)
    assert result == expected, f"Expected {expected}, but got {result}"
    
@pytest.mark.parametrize("list_dice,observation,state_sequence,transition_matrix", [(d, obs, ss, transition_matrix) 
                                                                                    for d in dice_data for obs in observations for ss in state_sequences])
def test_observation_state_sequence_joint_probability_computation_3f(list_dice, observation, state_sequence, transition_matrix):
    expected = observation_state_sequence_joint_probability_computation_correct(list_dice, observation, state_sequence, transition_matrix)
    result = observation_state_sequence_joint_probability_computation(list_dice, observation, state_sequence, transition_matrix)
    assert result == expected, f"Expected {expected}, but got {result}"
