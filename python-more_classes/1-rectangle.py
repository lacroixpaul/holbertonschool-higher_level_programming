#!/usr/bin/python3
"""
Module 0-rectangle
Provides an empty class Square that defines a square
"""


class Rectangle:
    """
        Provides an empty class Rectangle that defines a rectangle
    """
    pass

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter of the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the value of the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """ Getter of the heigth of the rectangle """
        return (self.__heigth)

    @heigth.setter
    def heigth(self, value):
        """ Set the value of the heigth of the rectangle """
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value
