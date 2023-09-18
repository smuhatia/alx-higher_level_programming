#!/usr/bin/python3
"""class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """a subclass of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class"""
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        """getting the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setting the setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting the width"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setting the setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting the x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setting the setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getting the y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """setting the setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """returns the area"""
        return self.__height * self.__width
    
    def display(self):
        """prints rectangle with #"""
        for h in range(self.y):
            print()
        for n in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """overides the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x , self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        up = ["id", "width", "height", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, up[i], args[i])

        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """Returns dict representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            'width': self.__width,
        }
