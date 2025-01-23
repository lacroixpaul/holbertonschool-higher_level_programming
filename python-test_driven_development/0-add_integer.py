#!/usr/bin/python3
"""
Module 0-add_integer
Provides a function `add_integer` to add two integers or floats.
"""


def add_integer(a, b=98):
    """
This function add two numbers.
Args:
    a (float or int): first number
    b (float or int): first number
Raises:
    TypeError : in case of non int or non float type argument
Returns:
    int: return the sum of a and b in a integer type.
Examples :
>>> add_integer(5, 5)
10
>>> add_integer(1.50, 2.25)
3
    """

    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if isinstance(a, float) and (a != a or a in (float('inf'), float('-inf'))):
        raise TypeError("a must be a valid number")

    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")
    if isinstance(b, float) and (b != b or b in (float('inf'), float('-inf'))):
        raise TypeError("b must be a valid number")

    return int(a) + int(b)
