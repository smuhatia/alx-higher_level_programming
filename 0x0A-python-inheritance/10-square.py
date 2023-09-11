#!/usr/bin/python3

"""importing BaseGeometry & Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""Write a class square that inherites from rectangle"""


class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """initialize private attribute size and validate it"""
        self.integer_validator("size", size)

        # here , we're calling the init method of the superclass Rectangle
        # we are doing this to avoid duplicating code.
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates  area of a square"""
        return self.__size ** 2
