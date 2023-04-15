#!/usr/bin/env python3

# The aim is to have a list in which all numbers do not appear more than once.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#

unique = []

for n in my_list:
    if n not in unique:
        unique.append(n)

my_list = unique

print("The list with unique elements only:")
print(my_list)
