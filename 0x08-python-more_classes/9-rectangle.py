#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """rect class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """intionialize the vale"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getting the valur of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting thr value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the eara of the ractangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """get perimeter of the regtangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """string presentation"""
        string = ""
        if self.__height != 0 and self.__width != 0:
            return ((str(self.print_symbol) * self.__width + "\n")
                    * self.__height)[:-1]

    def __repr__(self):
        """string repsentoin for developer"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delet instanse"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """get the biger value of eara of rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """new class method taht make a square rectangle
        args:
                size is the size of the new rectangle
        """
        return cls(size, size)
