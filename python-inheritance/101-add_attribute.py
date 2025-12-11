#!/usr/bin/python3
"""add attribute if possible"""


def add_attribute(obj, name, value):
    """add attribute if possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
