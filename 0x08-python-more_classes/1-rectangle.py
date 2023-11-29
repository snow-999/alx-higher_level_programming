#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """rect class"""
    def __init__(self, width=0, height=0):
        """intionialize the vale"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getting the valur of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting thr value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the value of height"""
        return self.height

    @height.setter
    def height(self, value):
        """setting the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
