#!/usr/bin/env python3

dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              } # hanging indents

phone_numbers = {
                'boss': 5551234567, 
                'Suzy': 22657854310
                }
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

words = ['cat', 'lion', 'horse']

print()

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print()

for key in dictionary.keys():
    print(key, "->", dictionary[key])

dictionary.update({"duck": "canard"})
print(dictionary)

del dictionary['dog']
print(dictionary)
