#!/usr/bin/python3

"""
0-read_file module
"""


def read_file(filename=""):
    """
    read a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
