#!/usr/bin/python3
"""Student class"""


class Student:
    """class of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs.__class__ is list and all(a.__class__ is str for a in attrs)):
            return {i: getattr(self, k) for i in attrs if hasattr(self, k)}:
        return self.__dict__
