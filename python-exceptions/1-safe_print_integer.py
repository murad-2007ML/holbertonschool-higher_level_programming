#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if len(value) >= 0:
            print("{} is not an integer".format(value))
            return False
    except:
        print("{:d}".format(value))
        return True
