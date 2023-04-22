#!/usr/bin/env python3

print('isalnum()')
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print('Six lambdas'.isalnum())
print('ΑβΓδ'.isalnum())
print('20E1'.isalnum())

print('\nisalpha()')
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

print('\nisdigit()')
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

print('\nislower()')
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

print('\nisspace()')
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

print('\nisupper()')
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

