#!/usr/bin/python3
"""input output task"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """find the attribute and return it"""
        try:
            for att in attrs:
                if type(att) != str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
