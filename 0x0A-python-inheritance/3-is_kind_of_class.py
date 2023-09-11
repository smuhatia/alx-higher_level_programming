#!/usr/bin/python3
""" checking the subclass"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is exactly a subclass of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
