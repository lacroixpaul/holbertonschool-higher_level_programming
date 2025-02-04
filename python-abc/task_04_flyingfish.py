#!/usr/bin/python3

"""
Module task_04_flyingfish.py
Provides an FlyingFish class
"""

from abc import ABC


class Fish:
    """
    class fish
    """

    def swim(self):
        """
        swim methode
        """
        print(f"The fish is swimming")

    def habitat(self):
        """
        habitat methode
        """
        print(f"The fish lives in water")


class Bird:
    """
    class bird
    """

    def fly(self):
        """
        fly methode
        """
        print(f"The bird is flying")

    def habitat(self):
        """
        habitat methode
        """
        print(f"The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class
    """

    def fly(self):
        """
        fly methode
        """
        print(f"The flying fish is soaring!")

    def swim(self):
        """
        fly methode
        """
        print(f"The flying fish is swimming!")

    def habitat(self):
        """
        habitat methode
        """
        print(f"The flying fish lives both in water and the sky!")
