#!/usr/bin/env python3

def is_palindrome(text):
    text = text.replace(' ', '').lower()

    return len(text) and text == text[::-1]

text = input('Enter some text: ')

if is_palindrome(text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
