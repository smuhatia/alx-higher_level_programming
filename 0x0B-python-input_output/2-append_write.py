#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 encoded file
    and returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
