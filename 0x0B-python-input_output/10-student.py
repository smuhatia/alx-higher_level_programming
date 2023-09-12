#!/usr/bin/python3
""" a class student with attributes"""


class Student:
    """
    Defines a Student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student with first_name, last_name, and age.
"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        attrs (list): A list of strings representing the attribute names.

        Returns:
        dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            # If attrs is None, return all attributes
            return self.__dict__
        else:
            # If attrs is a list of strings, return only those attributes
            return {attr: getattr(self, attr) for attr in
                    attrs if attr in self.__dict__}
