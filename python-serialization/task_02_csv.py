#!/usr/bin/python3

"""
task_02_csv.py
"""

import csv
import json


def convert_csv_to_json(filename):
    """
     takes the CSV filename and writes the JSON data to data.json
    """
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_fil:
            csv_reader = csv.DictReader(csv_fil)
            data = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
