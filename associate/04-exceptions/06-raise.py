#!/usr/bin/python3

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # No exception name. This can only be used inside except.

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
