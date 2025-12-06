#!/usr/bin/python3
def roman_to_int(roman_string):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    b = 0
    s = 0
    if type(roman_string) is not str or not roman_string:
        return 0
    else:
        for i in reversed(roman_string):
            if a[i] < b:
                s -= a[i]
            else:
                s += a[i]
            b = a[i]
    return s
