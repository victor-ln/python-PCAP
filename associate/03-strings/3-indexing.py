#!/usr/bin/env python3

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()


for ix in range(len(the_string) - 1, 0, -1):
    print(the_string[ix], end=' ')

print()

# Iterating through a string.

for character in the_string:
    print(character, end=' ')

print()

