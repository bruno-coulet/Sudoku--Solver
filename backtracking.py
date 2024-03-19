import os
from Grid import Grid


# The Solver class is used to solve a Sudoku puzzle.
class Solver(Grid):
    def __init__(self):
        Grid.__init__(self)

    # This method checks if a number can be placed in a specific spot on the grid.
    def is_valid(self, sudoku, row, col, num):
        for x in range(9):
            if sudoku[row][x] == num:
                return False
            if sudoku[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if sudoku[i + start_row][j + start_col] == num:
                    return False
        return True

    # This method solves the Sudoku puzzle using backtracking.
    def solve(self, sudoku, row=0, col=0):
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if sudoku[row][col] > 0:
            return self.solve(sudoku, row, col + 1)
        for num in range(1, 10):
            if self.is_valid(sudoku, row, col, num):
                sudoku[row][col] = num
                if self.solve(sudoku, row, col + 1):
                    return True
            sudoku[row][col] = 0
        return False

    # This method starts the solving process.
    def begin(self):
        self.file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
        sudoku = self.read_file(f"{self.file_name}.txt")
        self.display_grid(sudoku)
        if self.solve(sudoku):
            print("Sudoku résolu avec succès !")
            self.display_grid(sudoku)
        else:
            print("Pas de solution trouvée.")

# Create a Solver object and start the solving process.
solver = Solver()
solver.begin()
