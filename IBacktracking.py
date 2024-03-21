import time
from Files import Files
from Grid import Grid

class SudokuSolver(Grid,Files):
    def __init__(self):
        Grid.__init__(self)
        Files.__init__(self)
  
    def is_valid(self, sudoku, row, col, nb):
        # Check in the row
        if nb in sudoku[row]:
            return False

        # Check in the column
        for i in range(9):
            if sudoku[i][col] == nb:
                return False

        # Check in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if sudoku[i + start_row][j + start_col] == nb:
                    return False

        return True

    def find_empty(self, sudoku):
        # Find "_" in grid
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == '_':
                    return i, j
        return None, None

    def solve_sudoku(self, sudoku):
        # Find "_" in grid and got the position
        row, col = self.find_empty(sudoku)

        # Solver finish
        if row is None and col is None:
            return True

        # Change "_" --> 1 at 9
        for nb in map(str, range(1, 10)):
            if self.is_valid(sudoku, row, col, nb):
                sudoku[row][col] = nb

                # Call solver 1 by 1
                if self.solve_sudoku(sudoku):
                    return True

                # Return back
                sudoku[row][col] = '_'
        return False

    def run_solver(self, filename):
        start_time = time.time()

        sudoku = Files.read_file(filename)
        if self.solve_sudoku(sudoku):
            Files.save_change('sudoku_solution.txt', sudoku)

        end_time = time.time()  # Stop time
        self.solver_time = end_time - start_time # Calcul time

    def begin(self):
        print()
        self.file_name = input("Enter the Sudoku you want to solve : ")
        self.display_grid(f"input/{self.file_name}.txt")
        self.run_solver(f"input/{self.file_name}.txt")
        self.display_grid('sudoku_solution.txt')
        print("Time to solver :", self.solver_time, "seconds")
        print()

solver = SudokuSolver()
solver.begin()
