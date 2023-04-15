#!/usr/bin/env python3

# Objective:
#
# Assign the result of this expression:
# 3x³ - 2x² + 3x - 1 
# to y variable
#

# sample input
#
# x = 0
# x = 1
# x = -1
#

# expected output
#
# y = -1.0
# y = 3.0
# y = -9.0
#

x = 1 # hardcode your test data here
x = float(x)
# write your code here
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x - 1)
print("y =", y)
