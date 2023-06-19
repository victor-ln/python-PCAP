from functools import reduce

numbers = [float(input()) for _ in range(3)]

print(reduce(lambda total, x: total + x ** 2, numbers, 0))
