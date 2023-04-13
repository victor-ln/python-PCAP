#!/usr/bin/env python3

# Sample input: 1
# Expected output:
# y = 0.600000000000001

# Sample input: 10
# Expected output:
# y = 0.09901951266867294

# Sample input: 100
# Expected output:
# y = 0.009999000199950014

# Sample input: -5
# Expected output:
# y = -0.19258202567760344

x = float(input("Enter value for x: "))

# Write your code here.
y = 1 / (x + (1 / (x + (1 / (x + 1 / x)))))

print("y =", y)

