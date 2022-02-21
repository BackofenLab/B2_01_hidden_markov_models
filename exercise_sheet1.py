#!/user/bin/python3

from __future__ import division
from math import prod



# Exercise 1: Two kinds of dice
###############################

"""
A casino uses two kinds of dice: 98% of dice are fair and 2% are loaded. The loaded 
die has a probability of 0.5 to show number six and probability 0.1 for the numbers 
one to five.
"""

def exercise_1a():
    """
    Exercise 1 a
    When we pick up a die from a table at random, what is the probability of rolling a six?
    """
    probability = None
    return(probability)

def exercise_1b():
    """
    Exercise 1 b
    We pick up a die from a table at random and roll (6,6,6). What is the probability, that
    the die is loaded?
    """
    probability = None
    return(probability)

def exercise_1c():
    """
    Exercise 1 c
    How many sixes in a row would we need to roll to be at least 90% sure that the die is loaded?
    """
    probability = None
    return(probability)

# Exercise 2: The occasionally cheating casino
##############################################

"""
In a casino they use a fair die most of the time, but occasionally they switch to a loaded 
die. The loaded die has a probability 0.5 to show number six and probability 0.1 for the 
numbers one to five. Assume that the casino switches from a fair to a loaded die with 
probability 0.05 before each roll, and that the probability of switching back is 0.1. The 
probability to start a game with the fair die is 0.9.
"""

def exercise_2a():
    """
    Exercise 2 a
    Build the correct HMM graph. Match the letters from the blank figure to the numbers of \
    the correct parts in the parts lists!
    """
    partListA = None
    partListB = None
    partListC = None
    partListD = None
    partListE = None
    partListF = None
    partListG = None

    solution = [partListA,partListA,partListA,partListA,partListA,partListA,partListA]
    return(solution)
    
    
def exercise_2b():
    """
    Exercise 2 b
    Given an observed sequence of outcomes O = 3661634 and two possible state sequences \
    s1 = LLLFFFF and s2 = FFFFFFF (where F=fair and L=loaded), what are the joint probabilites \
    P(O,p1) and P(O,p2) in the HMM described above?
    """
    probability_0p1 = None
    prabability_0p2 = None
    return([probability_0p1,probability_0p2])

def exercise_2c():
    """
    Exercise 2 c
    Give an observation O = 1662, how many possible state sequences exist in the described HMM?
    """
    response = None
    return(response)


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

class Die:
    def __init__(self,P1,P2,P3,P4,P5,P6):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        self.P5 = P5
        self.P6 = P6
        self.probabilities = [P1,P2,P3,P4,P5,P6]
        
    def show_probabilities(self):
        p = [self.P1,self.P2,self.P3,self.P4,self.P5,self.P6]
        for i,j in enumerate(p):
            print("\t[-] P({})={}".format(i+1,j))

    def roll_prob(self,roll):
        """
        Exercise 3 a

        Implement the function roll_proba_given_dice which takes a list of dice and 
        a roll value and returns the probability of the roll. A roll is a single value 
        which can be obtained by throwing a die once.
        """
        if isinstance(roll,int):
            return(self.probabilities[roll])
        else:
            return(self.probabilities[int(roll)-1])

class Casino:
    def __init__(self):
        self.dice = []
        self.n = 0
        
    def add(self,Die):
        self.dice.append(Die)
        self.n+=1

    def show(self):
        for i, j in enumerate(self.dice):
            print("[+] Die {}:".format(i)); j.show_probabilities()
        
    def prob_observ_given_dice(self,observation):
        """
        Exercise 3 b
    
        Implement the function prob_observ_given_die which using the list of 
        dice and an observation and returns the probability of the observation.
        """
        probabilities = []
        for i in observation:
            prob_obs = sum([self.dice[j].roll_prob(i) * 1/self.n for j in range(self.n)])
            probabilities.append(prob_obs)
        return(prod(probabilities))

    def prob_die_given_observ(self,observation):
        """
        Exercise 3 c
    
        Implement the function proba_of_dice_given_observation which takes a list of 
        dice and an observation and returns the probability for each die to be used to 
        have the corresponding outcome.
        """
        probability_each_die = []
        for die in self.dice:
            obs_prob = []
            for i in observation:
                obs_prob.append(die.roll_prob(i)*(1/self.n)/self.prob_observ_given_dice(i))
            probability_each_die.append(prod(obs_prob))
        return(probability_each_die)

    def state_sequence_probability(state_sequence,transition_matrix):
        """
        Exercise 3 d
    
        Implement the function state_sequence_probability_computation which takes a 
        list of dice, a state sequence and the corresponding transition matrix for 
        the given dice and returns the probability of the state sequence.
        """

        probability_state_sequence = None
        return(probability_state_sequence)
    

    def prob_observ_given_state(observation,state_sequence):
        """
        Exercise 3 e
    
        Implement the function state_sequence_probability_computation which takes a 
        list of dice, a state sequence and the corresponding transition matrix for 
        the given dice and returns the probability of the state sequence.
        """

        probability_of_the_given_observation = None
        return(probability_of_the_given_observation)

    def observ_state_joint_probability(observation,state_sequence):
        """
        Exercise 3 f
    
        Implement the function observation_state_joint_probability which takes 
        a list of dice, an observation and a state sequence and return the joint 
        probability of the observation and the state sequence.
        """
    
        join_probability_observation,state_sequence = None
        return(join_probability_observation,state_sequence)

if __name__ == "__main__":
    dice1 = Die(1/6,1/6,1/6,1/6,1/6,1/6)
    dice2 = Die(1/2,1/10,1/10,1/10,1/10,1/10)
    casino = Casino()
    casino.add(dice1)
    casino.add(dice2)
    casino.show()
    print(casino.prob_observ_given_dice("12"))
    print(casino.prob_die_given_observ("12"))
