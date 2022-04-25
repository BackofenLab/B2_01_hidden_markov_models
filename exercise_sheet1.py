#!/user/bin/python3

from __future__ import division
from math import prod

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
    Exercise 3 a

    Implement the function roll_proba_given_die which takes a list of dice and
    a roll value and returns the probability of the roll. A roll is a single value
    which can be obtained by throwing a die once.
    """
    roll_proba = None
    return roll_proba

def observation_given_die(die, observation):
    """
    Exercise 3 b

    Implement the function prob_observ_given_die which using the list of
    dice and an observation and returns the probability of the observation.
    """
    observation_proba = None
    return observation_proba


def proba_of_dice_given_observation(list_dice, observation):
    """
    Exercise 3 c

    Implement the function proba_of_dice_given_observation which takes a list of
    dice and an observation and returns the probability for each die to be used to
    have the corresponding outcome.
    """
    list_dice_proba = None
    return list_dice_proba

def state_sequence_probability_computation(list_dice, state_sequence, transition_matrix):
    """
    Exercise 3 d

    Implement the function state_sequence_probability_computation which takes a
    list of dice, a state sequence and the corresponding transition matrix for
    the given dice and returns the probability of the state sequence.
    """
    state_sequence_probability = None
    return state_sequence_probability


def observation_probability_computation_given_state_sequence(list_dice, observation, state_sequence):
    """
    Exercise 3 e

    Implement the function state_sequence_probability_computation which takes a
    list of dice, a state sequence and the corresponding transition matrix for
    the given dice and returns the probability of the state sequence.
    """
    observation_probability = None
    return observation_probability

def observation_state_sequence_joint_probability_computation(list_dice, observation, state_sequence, transition_matrix):
    """
    Exercise 3 f

    Implement the function observation_state_joint_probability which takes
    a list of dice, an observation, a state sequence and a transition matrix, and return the joint
    probability of the observation and the state sequence.
    """
    state_sequence_proba = None
    obserbation_proba = None
    return None #state_sequence_proba * observation_proba
