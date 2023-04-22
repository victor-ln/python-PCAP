#!/usr/bin/env python3

def mysplit(string):
    arr = []

    string = string.strip()
    begin = 0
    end = string.find(' ')

    while end != -1:
        arr.append(string[begin:end])
        begin = end
        end = string.find(' ', end + 1)

    if len(string[begin:]):
        arr.append(string[begin:])

    return arr


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
