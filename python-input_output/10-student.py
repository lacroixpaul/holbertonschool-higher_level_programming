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

    def to_json(self):
        """
        returns the dictionary description with simple data structure
        """
        if isinstance(self, str):
            return {"first_name": self.first_name, "last_name": self.last_name}
        return self.__dict__
