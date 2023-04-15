#!/usr/bin/env python3

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 1, 2):
        if num % n == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
		print(i + 1, end=" ")
print()
