#!/usr/bin/python3
"""
Module 0-square.py
Provides an empty class Square that defines a square
"""


class Square:
    """
    Provides an empty class Square that defines a square

    Attribute :
        Size (private) of the square
    """

    def __init__(self, size=0):
        if size is not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
