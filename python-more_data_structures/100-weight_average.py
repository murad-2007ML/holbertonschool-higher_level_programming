#!/usr/bin/python3
def weight_average(my_list=[]):
    result, n = 0, 0
    for x, y in my_list:
        result += x * y
        n += y
    return 0 if n == 0 else result / n
