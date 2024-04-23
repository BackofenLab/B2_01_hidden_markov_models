#!/user/bin/python3

from __future__ import division
from math import prod
from tests.implementation import Die


# Exercise 3 - Programming Assignment
#####################################

"""
In this exercise you will be working with dice: namely probabilities of different rolls,
observations, state sequences etc. In order to make your experience better we implemented
a Die class for you.

You can create a die by simply providing the probabilities of the corresponding edges.
For example:

    > fair_die = Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
    > loaded_die = Die(0.1, 0.1, 0.1, 0.1, 0.1, 0.5)

You can access the value of the desired edge with two ways.

We prefer to start counting from zero so the probability of the first edge can be accessed
by its index (which is 0) like:

    > fair_die[0]

Alternatively the value on the first edge is 1, so the edge probability can be accessed by
the "name" of the edge and in this case we use the string value "1":

    > fair_die["1"]

We recommend sticking to the second way while solving the exercise.

Whenever we work with the set of dice we will define this set as a list of tuples. Each
tuple consists a pair: a die and the corresponding probability of picking the die.
For example:

    > fair_die = Die(1/6, 1/6, 1/6, 1/6, 1/6, 1/6)
    > loaded_die = Die(0.1, 0.1, 0.1, 0.1, 0.1, 0.5)

    > casino_dice = [(fair_die, 0.98), (loaded_die, 0.02)]
"""


def roll_proba_given_dice(list_dice, roll_value):
    """
    Calculate the probability of obtaining a specific roll value given a list of dice and their corresponding
    probabilities of being used.

    Args:
    list_dice: A list of tuples. Each tuple consists of a Die object and its probability of being used.
    roll_value: The roll value for which the probability is being calculated.

    Returns:
    float: The probability of obtaining the specified roll value.
    """

    roll_proba = None
    return roll_proba


def observation_given_die(die, observation):
    """
    Calculate the probability of a given observation (sequence of rolls) for a specific die.
    
    Args:
    die: A Die object.
    observation: A list of integers representing a sequence of rolls.
    
    Returns:
    float: The probability of the given observation for the specified die.
    """

    observation_proba = None
    return observation_proba


def proba_of_dice_given_observation(list_dice, observation):
    """
    Calculate the probability of each die being used, given a list of dice and an observation.
    
    Args:
    list_dice: A list of tuples. Each tuple consists of a Die object and its probability of being used.
    observation: A list of integers representing a sequence of rolls.
    
    Returns:
    list: A list of probabilities for each die to have produced the given observation.
    """

    list_dice_proba = None
    return list_dice_proba


def state_sequence_probability_computation(list_dice, state_sequence, transition_matrix):
    """
    Calculate the probability of a state sequence given a list of dice, the state sequence, and the
    corresponding transition matrix.
    
    Args:
    list_dice: A list of tuples. Each tuple consists of a Die object and its probability of being used.
    state_sequence: A list of integers representing a sequence of states.
    transition_matrix: A 2D list representing the transition probabilities between states.
    
    Returns:
    float: The probability of the given state sequence.
    """

    state_sequence_probability = None
    return state_sequence_probability


def observation_probability_computation_given_state_sequence(list_dice, observation, state_sequence):
    """
    Calculate the probability of an observation given a list of dice, the observation, and a state sequence.
    
    Args:
    list_dice: A list of tuples. Each tuple consists of a Die object and its probability of being used.
    observation: A list of integers representing a sequence of rolls.
    state_sequence: A list of integers representing a sequence of states.
    
    Returns:
    float: The probability of the given observation for the specified state sequence.
    """

    observation_probability = None
    return observation_probability


def observation_state_sequence_joint_probability_computation(list_dice, observation, state_sequence, transition_matrix):
    """
    Calculate the joint probability of an observation and a state sequence given a list of dice, the observation,
    the state sequence, and the corresponding transition matrix.
    
    Args:
    list_dice: A list of tuples. Each tuple consists of a Die object and its probability of being used.
    observation: A list of integers representing a sequence of rolls.
    state_sequence: A list of integers representing a sequence of states.
    transition_matrix: A 2D list representing the transition probabilities between states.
    
    Returns:
    float: The joint probability of the given observation and state sequence.
    """

    state_sequence_proba = None
    observation_proba = None
    return None # state_sequence_proba * observation_proba


if __name__ == "__main__":
    d = Die(0.5, 0.5)
    print(d)
