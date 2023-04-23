#!/usr/bin/env python3

# Objective:

# - asks when using a line of text to encrypt;
# - asks the user for an offset value (an integer in the range 1..25
# - note: should force the user to enter a valid offset value (don't give up and don't let bad data fool you!);
#
# - prints the encoded text.
#

text = input("Enter your message: ")

while True:
    try:
        offset = int(input("Enter the offset number in the range 1..25 inclusive: "))
        if offset not in range(1, 26):
            raise ValueError
        break
    except ValueError:
        print('Invalid input!')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_rotated = alphabet[offset:] + alphabet[:offset]

alphabet += alphabet.upper()
alphabet_rotated += alphabet_rotated.upper()

table = str.maketrans(alphabet, alphabet_rotated)

print(text.translate(table))
