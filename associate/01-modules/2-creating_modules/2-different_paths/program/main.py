#!/usr/bin/env python3 

from sys import path
from platform import system

# 'path' is a special variable (actually a list) that stores all the locations 
# (folders/directories) that are searched in order to find a module that has 
# been requested by the import statement. 
# 
# It is accessible through the module called sys

# Prints all paths searched for python interpreter when importing a module
#
# for p in sys.path:
#     print(p)

if system() == 'Linux':
    path.append('../modules')
else:
    path.append('..\\modules')

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
