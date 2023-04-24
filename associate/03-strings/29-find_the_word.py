#!/usr/bin/env python3

# Are the characters making up the first string hidden within the second string?
#
# Example:
#
# if the second string is given as “vcxzxduybfdsobywuefgas”, the answer is yes;
#
# if the second string is “vcxzxdcybfdstbywuefsas”, the answer is no 
# (since there are no letters “d”, “o”, or “g”, in that order)
#

def found_hidden_word(word, where_to_find):
    it = iter(where_to_find)
    return all(ch in it for ch in word)

to_find = input('Enter a string to find: ')
where_find = input('Enter where to find: ')

if found_hidden_word(to_find, where_find):
    print('Yes')
else:
    print('No')
