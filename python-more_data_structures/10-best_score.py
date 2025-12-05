#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return None
    else:
        maximum = max(a_dictionary, key = a_dictionary.get)
        return maximum
