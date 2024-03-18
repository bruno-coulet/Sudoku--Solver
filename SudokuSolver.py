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
