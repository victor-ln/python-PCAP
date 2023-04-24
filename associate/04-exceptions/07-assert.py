#!/usr/bin/python3

import math

x = float(input("Enter a number: "))

# If the expression evaluates to True, or a non-null numeric value, or 
# a non-empty string, or any other value other than None, it does nothing else;
# Otherwise, it automatically and immediately raises an exception 
# called AssertionError (in this case, we say that the assertion failed)

assert x >= 0.0

x = math.sqrt(x)

print(x)
