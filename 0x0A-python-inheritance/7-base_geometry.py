#!/usr/bin/python3
"""7-base_geometry.py"""


class BaseGeometry:
    """Implements a basic geometric shape"""

    def area(self):
        """Raises Exception with message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value of a given name
        Args:
            name: string
            value: integer value of given name
        Returns: None
        """
        # if value is not an integer
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        # if value is less or equal to 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
