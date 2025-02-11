#!/usr/bin/python3

"""
task_01_pickle.py
"""

import pickle


class CustomObject:
    """
    class CustomObject
    """

    def __init__(self, name, age, is_student):
        """
        initialize the class CustomObject
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        print out the attribute
        """
        for attribut, valeur in self.__dict__.items():
            print(f"{attribut}: {valeur}")

    def serialize(self, filename):
        """
        serialize the current instance and save it to the provided filename.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        load and deserialize data from the specified file
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            return None
