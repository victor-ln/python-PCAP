#!/usr/bin/env python3

def has_duplicates(list):
    return len(set(list)) != 9

def is_sudoku_valid(sudoku: list):
    turned_sudoku = [list(col) for col in zip(*sudoku)]

    for x in range(9):
        if has_duplicates(sudoku[x]) or \
            has_duplicates(turned_sudoku[x]):
            return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            square = [sudoku[x + i][y + j] for i in range(3) for j in range(3)]
            if has_duplicates(square):
                return False

    return True

sudoku = []
print('Enter the sudoku game')

for row in range(9):
    numbers_str = input()
    numbers = [int(number) for number in numbers_str]
    sudoku.append(numbers)

if is_sudoku_valid(sudoku):
    print('Yes')
else:
    print('No')
