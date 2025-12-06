#!/usr/bin/python3
def weight_average(my_list=[]):
    result, n = 0, 0
    for i in my_list:
        h = 1
        n += i[1]
        for j in i:
            h = h * j
        result += h
    return result / n
