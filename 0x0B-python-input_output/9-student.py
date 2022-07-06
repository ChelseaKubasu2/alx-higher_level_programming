#!/usr/bin/python3
"""9-student Module
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises the first_name, last_name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return vars(self)
