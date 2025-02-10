#!/usr/bin/python3

"""
7-add_item.py
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    def add_arguments_to_json():
        """
        adds all arguments to a Python list, and then save them to a file:
        """
        arguments = sys.argv[1:]
        data = load_from_json_file("add_item.json")
        data.extend(arguments)
        save_to_json_file(data, "add_item.json")
