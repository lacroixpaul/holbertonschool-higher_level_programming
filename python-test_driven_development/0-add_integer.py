#!/usr/bin/python3
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

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a is float:
        int(a)
    if b is float:
        int(b)
    return int(a) + int(b)
