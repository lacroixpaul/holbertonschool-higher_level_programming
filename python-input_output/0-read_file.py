#!/usr/bin/python

"""
read_file module
"""


def read_file(filename=""):
    """
    read a file
    """
    with open(filename, "r") as f:
        contents = f.read
        print(contents)
