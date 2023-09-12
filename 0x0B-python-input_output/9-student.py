#!/usr/bin/python3
"""a class Student that defines a student by first_name,
last_name and age"""


class Student:
    """
    Defines a Student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student with first_name, last_name, and age.

        Parameters:
        first_name (str): The first name of the Student.
        last_name (str): The last name of the Student.
        age (int): The age of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        dict: A dictionary representation of the Student instance.
        """
        return self.__dict__
