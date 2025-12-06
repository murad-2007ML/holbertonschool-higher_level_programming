#!/usr/bin/python3
def roman_to_int(roman_string):
    import roman
    if not roman_string:
        return 0
    else:
        return roman.fromRoman(roman_string)
