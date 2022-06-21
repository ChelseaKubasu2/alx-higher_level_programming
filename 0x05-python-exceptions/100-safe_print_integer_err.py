#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format()
    Args:
        value: value to be printed
    Return: True if successful.Otherwise False
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    else:
        return True
