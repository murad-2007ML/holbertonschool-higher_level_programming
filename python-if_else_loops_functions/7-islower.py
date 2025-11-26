#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return True
    else:
        return False
a = input()
if True:
    print(a," is {}".format("lower" if islower(a) else "upper"))
