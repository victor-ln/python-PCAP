#!/usr/bin/env python3

blocks = int(input("Enter the number of blocks: "))

height = 1
summed_blocks = 1
while (summed_blocks + height < blocks):
    height += 1
    summed_blocks += height

# The triangular numbers are given by the following explicit formula:
# Tn = (n(n + 1)) / 2

# n ^ 2 + n - 2Tn = 0
# a ^ 2 + b - c = 0

# delta = 1 - 4 * (-2 * blocks)
# height = (-1 + delta ** 0.5) // 2

print("The height of the pyramid:", height)
