#!/usr/bin/python3

"""
10-student.py
"""


class Student:
    """
    class Student
    """

    def __init__(self, first_name, last_name, age):
        """ Initialize the square """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns the dictionary description with simple data structure
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if isinstance(attr, str) and attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
