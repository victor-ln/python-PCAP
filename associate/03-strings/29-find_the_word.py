#!/usr/bin/env python3

to_find = input('Enter a string to find: ')
where_find = input('Enter where to find: ')

def find_in_letters(to_find, where_find):
    pos = 0
    for letter in to_find:
        pos = where_find.find(letter, pos)
        if pos == -1:
            print('No')
            return
    print('Yes')

find_in_letters(to_find, where_find)
