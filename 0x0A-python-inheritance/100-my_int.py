#!/usr/bin/python3
""" In this code, __eq__ and __ne__ methods are overridden to invert
the == and != operators. The int.__ne__ and int.__eq__ are the original
methods from the int class that we still have access to via the parent class.
"""


class MyInt(int):
    """MyInt is a subclass of int with == and != operators inverted"""

    def __eq__(self, other):
        """Override == operator : return not equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Override != operator : return equal"""
        return int.__eq__(self, other)
