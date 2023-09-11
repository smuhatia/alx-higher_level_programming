#!/usr/bin/python3
""" Full rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class that inherits from BaseGeometry """
    def __init__(self, width, height):
        """
        Initializes width and height.
        Value validation by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return the print() and str() representation """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
