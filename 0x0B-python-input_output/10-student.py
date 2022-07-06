#!/usr/bin/python3
"""10-student Module
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises the first_name, last_name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list and all([type(s) == str for s in attrs]):
            return {key: value for key, value in vars(self).items()
                    if key in attrs}

        return vars(self)
