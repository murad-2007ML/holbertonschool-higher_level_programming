#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Defines a Rectangle"""
    
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    
    @property
    def width(self):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.__width = width
    
    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        return self.__width
    
    @property
    def height(self):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height
    
    @height.setter
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        return self.__height
