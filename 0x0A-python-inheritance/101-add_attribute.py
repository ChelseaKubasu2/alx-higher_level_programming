#!/usr/bin/python3
"""101-add_attribute.py"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible
    Args:
        object: object whose attribute has to be set
        name: attribute name
        value: value given to the attribute
    Returns: None
    """
    # check if obj contains the __dict__() method
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
