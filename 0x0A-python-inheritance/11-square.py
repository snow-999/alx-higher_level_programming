#!/usr/bin/python3
"""make an square class that was inhartance from the rectangle"""
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
        return self.__size ** 2

    def __str__(self):
        """get the presentation of the the user veiw"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
