#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Create an empty class"""
    def area(self):
        raise Exceptation("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        if not isinstance(self.value, int):
            raise TypeError(f"{name} must be an integer")
        elif self.value <= 0:
            raise ValueError(f"{name} must be greater than 0")
