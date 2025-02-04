#!/usr/bin/python3

"""
Module task_01_abc.py
Provides an ABC class Shape
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    ABC class Shape
    """

    @abstractmethod
    def area(self):
        """
        area ABC method
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter ABC method
        """
        pass


class Circle(Shape):
    """
    Circle class
    """

    def __init__(self, radius):
        """
        Initialize the Circle class
        """
        self.radius = radius

    def area(radius):
        """
        area method
        """
        return 3.14 * radius ** 2

    def perimeter(radius):
        """
        perimeter method
        """
        return 3.14 * radius * 2


class Rectangle(Shape):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle class
        """
        self.width = width
        self.height = height

    def area(width, height):
        """
        area method
        """
        return width * height

    def perimeter(width, height):
        """
        perimeter method
        """
        return 2 * (height + width)
