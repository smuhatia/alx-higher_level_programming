#!/usr/bin/python3
"""
in this code Mylist inherits from list, which means
it gets all the properties and methods of a list then uses
the function print_sorted to print a sorted list
"""


class MyList(list):
    """passing the base class list to Mylist"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """ it prints the sorted list"""
        print(sorted(self))
