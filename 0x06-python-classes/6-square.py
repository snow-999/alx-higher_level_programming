#!/usr/bin/python3
"""get the size of sqare"""


class Square:
    """get the size of sqare"""

    def __init__(self, size=0, position=(0, 0)):
        """get the size of sqare"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size of the sqare"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get postion to value"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(num >= 0 for num in value) or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """get the erea of sqare"""
        return self.__size * self.__size

    def my_print(self):
        """print the sqare of #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for y in range(0, self.__size)]
            print("")
