#!/usr/bin/env python3

# Importing 'sin' and 'pi' from the 'math' module
from math import sin, pi

# Printing the value of sin(pi * .5) using the 'sin' function from the 'math' module
print(sin(pi * .5))

# This would cause an error, only 'sin' and 'pi' were imported from math into this namespace
# print(math.e)

# Redefining the value of 'pi' to 3.14
pi = 3.14

# Defining a local function 'sin' that takes an argument 'rad'
# This function rewrites the definition of 'sin' into the current namespace
def sin(rad):
    if (rad * 2 == pi):
        return 0.99999999
    return None

# Printing the value of sin(pi * .5) using the local 'sin' function
# Note: This will now use the local function 'sin' with the custom value, not the 'sin' function from the 'math' module
print(sin(pi * .5))
