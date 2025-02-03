#!/usr/bin/python3
"""
Module 8-base_geometry.py
Provides a class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Child class Square of Rectangle
    """

    def __init__(self, size):
        """
        Initialize the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Define area of the square
        """
        return self.__size * self.__size
