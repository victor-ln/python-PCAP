#!/usr/bin/env python3 

# When Python imports a module for the first time, 
# it translates its contents into somewhat compiled form.
#
# The file does not contain machine code - it is semi-compiled Python 
# internal code, ready to be executed by the Python interpreter. 
# As such, a file does not require many of the checks required for 
# a pure source file, execution starts faster, and runs faster as well.
#
# Thanks to this, each subsequent import will be faster 
# than interpreting the source text from scratch.
#
# Python is able to check if the module's source file has been modified 
# (in this case the pyc file will be rebuilt) or not 
# (when the pyc file can be executed at once). 
#
# As this process is fully automatic and transparent, 
# you don't need to keep it in mind.
#

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
