#!/usr/bin/python3
"""Direct or indirect"""


def inherits_from(obj, a_class):
    """It finds out it's directly inherited or not"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
