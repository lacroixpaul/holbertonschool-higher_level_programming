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
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if not isinstance(attr, str) or attr not in self.__dict__:
                    return self.__dict__
                result[attr] = self.__dict__[attr]
            return result
        return self.__dict__
