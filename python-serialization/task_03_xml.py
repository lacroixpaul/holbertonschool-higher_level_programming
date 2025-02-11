#!/usr/bin/python3

"""
task_03_xml.py
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize a python dictionary into XML and save it to the given filename
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
        return True
    except Exception as e:
        return False


def deserialize_from_xml(filename):
    """
    return a deserialized Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        key = child.tag
        value = child.text
        if value.isdigit():
            value = int(value)
        elif value.replace(".", "", 1).isdigit() and value.count(".") == 1:
            value = float(value)
        dictionary[key] = value
    return dictionary
