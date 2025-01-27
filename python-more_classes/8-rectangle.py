#!/usr/bin/python3
"""
Module 7-rectangle
Provides an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
        Provides an empty class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter of the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the value of the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the value of the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Returns a string to print the rectangle with # """
        if self.__width == 0 or self.__height == 0:
            return ""
        if isinstance(self.print_symbol, list):
            elements = [f"'{element}'" for element in self.print_symbol]
            print_symbol_str = '[' + ', '.join(elements) + ']'
        else:
            print_symbol_str = str(self.print_symbol)
        return "\n".join([print_symbol_str * self.width] * self.height)

    def __repr__(self):
        """ Return a string which describe the object """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Print a message when an instance is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area2:
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """  returns a new Rectangle instance with width == height == size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return cls(size, size)
