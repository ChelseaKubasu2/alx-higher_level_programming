#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """Implements a class that inherits from int"""

    def __eq__(self, other):
        """Defines behavior for '=='"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Defines behavior for '!='"""
        return super().__eq__(other)
