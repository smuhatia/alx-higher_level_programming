#!/usr/bin/python3
""" a class student"""


class Student:
    """
    Defines a Student by first name, last_name, and age.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        attrs (list): A list of strings representing the
        attribute names to be retrieved.

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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        those in the provided json dictionary.

        Parameters:
        json (dict): A dictionary where the key is the public attribute
        name and the value is the value of the public attribute.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
