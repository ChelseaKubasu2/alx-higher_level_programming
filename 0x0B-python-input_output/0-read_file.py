#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: text file to read
    Returns: None
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
