#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: python object to write to the given file
        filename: name of the file to write object to
    Returns: None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
