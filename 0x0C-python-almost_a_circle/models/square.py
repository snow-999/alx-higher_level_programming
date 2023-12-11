#!/usr/bin/python3
""" square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square  class"""
    def __init__(self, size, x=0, y=0, id=None):
        """intionlaz the attribute"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print presntion for user view"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getting the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the value of size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """get the arguments"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
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
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
