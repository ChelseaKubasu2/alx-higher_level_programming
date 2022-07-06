#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
        filename: name of JSON file to decode to object
    Returns: object decoded from filename
    """
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)

    return obj
