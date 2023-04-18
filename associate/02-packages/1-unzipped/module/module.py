#!/usr/bin/env python3 

# a string (perhaps a multiline) placed before any module statement 
# (including imports) is called the doc-string, and should briefly 
# explain the purpose and contents of the module

""" module.py - an example of a Python module """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

# When a Python file is run directly as a script, i.e. not imported as a module 
# in another file, the value of __name__ is set to __main__

if __name__ == "__main__":
    # Code to be executed only when the file is executed directly as a script
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i + 1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

