#!/usr/bin/python3
""" main file"""


def say_my_name(first_name, last_name=""):
    """
    This function receives a first name and last name and print them
    """
    # These first two conditionals check if 'first_name' and 'last_name'
    # are strings. If they're not, the function raises a TypeError.
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # This is where the function prints out the statement.
    print("My name is {:s} {:s}".format(first_name, last_name))
