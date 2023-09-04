#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """ define a class with with width and height attributes"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the rectangle
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """prints a rectangle using # symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            my_list = ""
            for j in range(self.__height):
                for i in range(self.__width):
                    my_list += str(self.print_symbol)
                if (j != self.__height - 1):
                    my_list += "\n"
            return (my_list)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ decrement number of instances upon deletion of instance"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
