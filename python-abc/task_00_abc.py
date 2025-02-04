#!/usr/bin/python3

"""
Module task_00_abc.py
Provides an ABC class Animal with two subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    ABC class Animal
    """

    @abstractmethod
    def sound(self):
        """
        sound ABC method
        """
        pass


class Dog(Animal):
    """
    Dog class
    """

    def sound(self):
        """
        Sound method
        """
        return ("Bark")


class Cat(Animal):
    """
    Cat class
    """

    def sound(self):
        """
        Sound method
        """
        return ("Meow")
