#!/usr/bin/python3
"""get a new inhartance class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """"initialize attributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """get the area of the square"""
        return self.__size * self.__size
