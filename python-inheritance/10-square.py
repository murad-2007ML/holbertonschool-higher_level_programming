#!/usr/bin/python3
"""Inhertitance from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inhertitance from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
