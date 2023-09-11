#!/usr/bin/python3
"""
Check if the object has a __dict__ attribute using hasattr function.
If it does, add the new attribute using setattr function.
If it doesn't, raise a TypeError with the message "can't add new attribute".
"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
