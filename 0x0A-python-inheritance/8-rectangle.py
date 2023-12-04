#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """new class iinhertance from last class"""
    def __init__(self, width, height):
        """initialize the new attrebutes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
