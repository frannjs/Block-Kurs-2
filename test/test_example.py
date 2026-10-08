# Your testing code

from src.my_math import *

def test_add_numbers():
    result = add_numbers(1,2)
    assert result == 3

def test_substract_numbers():
    result = subtract_numbers(8,5)
    assert result == 3

def test_multiply_numbers():
    result = multiply_numbers(9,5)
    assert result == 45
