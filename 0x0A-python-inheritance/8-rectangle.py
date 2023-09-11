#!/usr/bin/python3
""" rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a subclass of BaseGeometry class"""

    def __init__(self, width, height):
        """ itializes private attributes"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
