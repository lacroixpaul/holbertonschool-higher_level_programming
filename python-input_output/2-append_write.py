#!/usr/bin/python3

"""
2-append_write.py
"""


def append_write(filename="", text=""):
    """
    append a file and count nb of added characters
    """
    with open(filename, "a") as fichier:
        fichier.write(text)
        return len(text)
