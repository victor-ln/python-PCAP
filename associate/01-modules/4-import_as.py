#!/usr/bin/env python3

# Importing the 'sin' function from the 'math' module and renaming it to 'sine' using the 'as' keyword
# 'sine' now is an alias for the 'sin' function from the 'math' module
from math import sin as sine, pi as PI

# Printing the value of sine(PI * .5) using the renamed 'sine' function and the renamed 'PI' constant
# 'sine' refers to the 'sin' function from the 'math' module, but using the alias 'sine'
# 'PI' refers to the constant 'pi' provided by the 'math' module, but also using the alias 'PI'
print(sine(PI * .5))
