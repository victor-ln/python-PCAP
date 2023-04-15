#!/usr/bin/env python3

n = int(input("Enter a number: "))
steps = 0

while True:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1
    print(n)
    if n == 1:
        break

print("Steps =", steps)
