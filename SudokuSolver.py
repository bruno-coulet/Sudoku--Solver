import random

class SudokuSolver:
    def __init__(self):
        pass
    # Replace the underscores with random numbers
    def random_replace(self, sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == '_':
                    sudoku[i][j] = str(random.randint(1, 9))
    # Load the sudoku from a file
    def read_sudoku(self, filename):
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(line.strip())
                sudoku.append(row)
        return sudoku
    # Save the sudoku to a file
    def save_change(self, filename, sudoku):
        with open(filename, 'w') as file:
            for row in sudoku:
                file.write(''.join(row) + '\n')