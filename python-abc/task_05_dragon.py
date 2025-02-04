#!/usr/bin/python3

"""
Module task_05_dragon.py
Provides an CountedIterator class
"""

from abc import ABC


class SwimMixin:
    """
    class SwimMixin
    """

    def swim(self):
        """
        swim methode
        """
        print(f"The creature swims!")


class FlyMixin:
    """
    class FlyMixin
    """

    def fly(self):
        """
        fly methode
        """
        print(f"The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    class Dragon
    """

    def roar(self):
        """
        roar methode
        """
        print(f"The dragon roars!")


draco = Dragon()
draco.fly()
draco.swim()
draco.roar()
