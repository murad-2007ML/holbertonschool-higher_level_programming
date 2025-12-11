#!/usr/bin/python3
"""add attribute if possible"""


def func(obj, name, value):
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
