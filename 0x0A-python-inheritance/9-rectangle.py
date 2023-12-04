#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """new class iinhertance from last class"""
    def __init__(self, width, height):
        """initialize the new attrebutes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """fonction to get the eara"""
        return self.__height * self.__width

    def __str__(self):
        """method to print to the user"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
