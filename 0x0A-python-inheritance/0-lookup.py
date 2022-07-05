#!/usr/bin/python3
"""0-lookup.py"""


def lookup(obj):
    """lists the available attributes and methods of an object
    Args:
        obj: object whose attributes and methods to list
    Returns: list of available attributes and methods of obj
    """
    return list(dir(obj))
