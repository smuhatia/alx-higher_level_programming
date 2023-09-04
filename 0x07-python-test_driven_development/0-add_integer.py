#!/usr/bin/python3
""" a function that adds 2 integers"""


def add_integer(a, b=98):
    """ returns the sum of 2 integers

    Args:
    a: first integer
    b: second integer

    Returns:
    a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
