#!/usr/bin/env python3

secret_word = "chupacabra"

while True:
    guess = input("Guess the secret word: ")
    if (guess == secret_word):
        break
    print("Not this word")

print("You've successfully left the loop.")
