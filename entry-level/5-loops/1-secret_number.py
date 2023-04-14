#!/usr/bin/env python3

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""") # Multi-Line printing

while int(input("Guess the secret number: ")) != secret_number:
    print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")
