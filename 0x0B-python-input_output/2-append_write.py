#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    Args:
        filename: file to write to
        text: text to write in in given file
    Return: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)

    return count
