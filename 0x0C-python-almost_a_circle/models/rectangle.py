#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class that inhertce from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        self.validation_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the vlaue of the height"""
        self.validation_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        self.validation_int("x", value)
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        self.validation_int("y", value)
        self.__y = value

    def validation_int(self, name, value, quality=True):
        """validation function"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if quality and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not quality and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """get the erea of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """print # as rectangle"""
        dis_str = "\n" * self.y + \
            (" " * self.x + "#" * self.width + "\n") * self.height
        print(dis_str, end="")

    def __str__(self):
        """print for user view"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """get the arguments"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """get an arguments"""
        if args:
            self.__update(*args)
        else:
            self.__update(**kwargs)

    def to_dictionary(self):
        """retturn repersentaion"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
