#!/usr/bin/python3

"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write a file and count nb of characters
    """
    with open(filename, "w") as fichier:
        fichier.write(text)
        return len(text)
