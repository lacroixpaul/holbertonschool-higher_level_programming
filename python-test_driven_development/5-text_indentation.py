#!/usr/bin/python3
"""
Module 5-text_indentation
Provides a function `text_indentation` to indent a string
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The string to indent.

    Returns:
        None

    Raises:
        TypeError: If str is not an string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
