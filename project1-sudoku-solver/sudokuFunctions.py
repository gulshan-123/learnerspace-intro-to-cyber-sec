sudoku = [
    [-1, -1, 3, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [7, -1, -1, 1, -1, 3, -1, 5, -1],
    [-1, -1, -1, 3, -1, -1, 8, -1, 7],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [-1, -1, -1, -1, -1, -1, -1, 6, -1],
    [-1, -1, 1, -1, -1, -1, 9, 7, -1],
    [-1, -1, 2, -1, -1, 8, -1, -1, -1],
    [-1, -1, -1, 5, -1, -1, -1, -1, 2]
]

def print_sudoku(sudoku):
    for row in sudoku:
        print(row)

def is_valid(sudoku, row, col, num):
    # Check if the number is in the row
    if num in sudoku[row]:
        return False

    # Check if the number is in the column
    if num in [sudoku[i][col] for i in range(9)]:
        return False

    # Check if the number is in the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False

    return True

def solve_sudoku(sudoku_):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == -1:
                for num in range(1, 10):
                    if is_valid(sudoku, i, j, num):
                        sudoku[i][j] = num
                        if (solve_sudoku(sudoku)):
                            return True
                        sudoku[i][j] = -1
                return False
    return True

def compare_sudoku(sudoku, sudoku2):
    differences = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] != sudoku2[i][j]:
                differences.append((i, j, sudoku2[i][j]))
    return differences
