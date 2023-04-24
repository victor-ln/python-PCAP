#!/usr/bin/python3

def read_int(prompt, min, max):

    while True:
        try:
            v = int(input(prompt))
            if v in range(min, max):
                return v
            print('Error: the value is not within permitted range (-10..10)')
        except:
            print('Error: wrong input')

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
