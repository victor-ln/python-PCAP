#!/usr/bin/env python3

def are_anagrams(text1: str, text2: str):
    text1 = text1.replace(' ', '').lower()
    text2 = text2.replace(' ', '').lower()

    return len(text1) and len(text2) and sorted(text1) == sorted(text2)

text1 = input('Enter text1: ')
text2 = input('Enter text2: ')

if are_anagrams(text1, text2):
    print("Anagrams")
else:
    print("Not anagrams")
