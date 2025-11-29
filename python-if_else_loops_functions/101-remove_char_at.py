#!/usr/bin/python3
def remove_char_at(str, n):
    a = ""
    for i in range(len(str)):
        if i == n:
            continue
        a += str[i]
    return a
