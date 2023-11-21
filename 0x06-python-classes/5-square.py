#!/usr/bin/python3
"""get the size of sqare"""


class Square:
    """get the size of sqare"""

    def __init__(self, size=0):
        """get the size of sqare"""
        self.__size = size

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """check the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get the erea of sqare"""
        return self.__size * self.__size 

    def my_print(self):
        for i in range(self.size):
            for x in range(self.size):
                if x == self.size -1 and i != x:
                    print("#")
                else:
                    print("#", end="")
        print()
