#!/usr/bin/python3
"""get the size of sqare"""


class Square:
    """get the size of sqare"""

    def __init__(self, size=0):

        """get the size of sqare"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """get the area of sqare"""
        return self.__size * self.__size
