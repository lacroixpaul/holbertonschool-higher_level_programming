#!/usr/bin/python3

"""
Module task_01_abc.py
Provides an ABC class Shape
"""

from abc import ABC, abstractmethod
import math


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

    def area(self):
        """
        area method
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        perimeter method
        """
        return math.pi * self.radius * 2


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

    def area(self):
        """
        area method
        """
        return self.width * self.height

    def perimeter(self):
        """
        perimeter method
        """
        return 2 * (self.height + self.width)


def shape_info(shape):
    """
    shape_info methode
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":

    circle_1 = Circle(5)
    rectangle_1 = Rectangle(4, 7)

    shape_info(circle_1)
    shape_info(rectangle_1)
