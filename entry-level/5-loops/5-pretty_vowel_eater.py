#!/usr/bin/env python3

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    # Complete the body of the for loop.
    if letter in 'AEIOU':
        continue
    word_without_vowels += letter

print(word_without_vowels)
