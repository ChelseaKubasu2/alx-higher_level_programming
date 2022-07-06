#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    Args:
        filename: file to write to
        text: text to write in in given file
    Return: the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)

    return count
