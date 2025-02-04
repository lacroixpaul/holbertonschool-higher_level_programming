#!/usr/bin/python3

"""
Module task_03_countediterator.py
Provides an CountedIterator class
"""

from abc import ABC


class CountedIterator:
    """
    class CountedIterator
    """
    def __init__(self, iterable):
        """
        Initialize the class
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        next method
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        get_count method
        """
        return self.count

    def __iter__(self):
        """Return the iterator itself."""
        return self
