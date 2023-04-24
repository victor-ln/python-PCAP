#!/usr/bin/env python3

birthday = input('Enter your birthday: ')

while len(birthday) > 1:
    birthday = str(sum([int(digit) for digit in birthday]))

print('Your life digit is:', birthday)
