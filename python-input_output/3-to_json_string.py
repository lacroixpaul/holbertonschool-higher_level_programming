#!/usr/bin/python3
import json

"""
3-to_json_string.py
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    my_obj_json = json.dumps(my_obj)
    return my_obj_json
