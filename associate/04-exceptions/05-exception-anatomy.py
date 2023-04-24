#!/usr/bin/python3

# - The order of the branches is important!
# - Don't put more general exceptions before more concrete exceptions;
# - This will make the latter unattainable and useless;

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")

