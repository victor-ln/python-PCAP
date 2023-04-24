#!/usr/bin/env python3

def has_duplicates(sudoku):
    return any(len(set(row)) != 9 for row in sudoku)

def is_sudoku_valid(sudoku):
    if has_duplicates(sudoku):
        return False

    if has_duplicates([col for col in zip(*sudoku)]):
        return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            square = set(sudoku[x + i][y + j] for i in range(3) for j in range(3))
            if len(square) != 9:
                return False

    return True

sudoku = []
print('Enter the sudoku game')

for row in range(9):
    sudoku.append(list(input()))

if is_sudoku_valid(sudoku):
    print('Yes')
else:
    print('No')
