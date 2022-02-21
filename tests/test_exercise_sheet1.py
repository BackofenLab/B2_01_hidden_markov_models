from __future__ import division
from math import isclose, prod
import pytest
from random import seed
from helpers.helpers import *
from exercise_sheet1 import *

seed(10)

N_TESTS = 10
DICE_PROBABILITIES = [1/10,1/10,1/10,2/10,2/10,3/10]

def test_exercise_1a():
    """
    For details check README spoilers.
    """
    response = exercise_1a()
    solution = 0.98 * (1/6) + 0.02 * 0.5
    assert isclose(response,solution,abs_tol=1e-3)

def test_exercise_1b():
    """
    For details check README spoilers.
    """
    response = exercise_1b()
    solution = (0.5**3*0.02)/(0.5**3*0.02+(1/6)**3*0.98)
    assert isclose(response,solution,abs_tol=1e-3)

def test_exercise_1c():
    """
    For details check README spoilers.
    """
    response = exercise_1c()
    solution = 5.542487
    assert isclose(response,solution,abs_tol=1e-3)

def test_exercise_2a():
    """
    For details check README.
    """
    response = [int(x) for x in exercise_2a()]
    solution = [2,6,4,5,1,1,5]
    assert response == solution

def test_exercise_2b():
    """
    For details check README spoilers.
    """
    response = exercise_2b()
    solution = [1.34*10**(-7), 2.36*10**(-6)]
    assert response == solution

def test_exercise_2c():
    """
    For details check README spoilers.
    """
    response = int(exercise_2c())
    solution = 16
    assert response == solution
    
def test_exercise_3a():
    """
    For details check README.
    """
    
def test_exercise_3b():
    """
    For details check README.
    """
    
def test_exercise_3c():
    """
    For details check README.
    """
    
def test_exercise_3d():
    """
    For details check README.
    """
    
def test_exercise_3e():
    """
    For details check README.
    """
    
def test_exercise_3f():
    """
    For details check README.
    """
