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

    def area(self):
        """
        area method
        """
        return 3.141592653589793 * self.radius ** 2

    def perimeter(self):
        """
        perimeter method
        """
        return 3.141592653589793 * self.radius * 2


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


def shape_info(obj):
    """
    shape_info methode
    """
    obj_area = obj.area()
    obj_perimeter = obj.perimeter()
    print(f"Area: {obj_area}")
    print(f"Perimeter: {obj_perimeter}")


circle_1 = Circle(5)
rectangle_1 = Rectangle(4, 7)

shape_info(circle_1)
shape_info(rectangle_1)
