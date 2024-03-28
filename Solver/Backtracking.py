from Solver.Files import Files
from Solver.Grid import Grid
import time

class Backtracking(Grid,Files):
    def __init__(self):
        Grid.__init__(self)
        Files.__init__(self)
        self.result = False
        
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
        self.start_time = time.time()
        
        row, col = self.find_empty(sudoku)

        # Solver finish
        if row is None and col is None:
            return True

        # Change "_" --> 1 at 9
        for nb in map(str, range(1, 10)):
            if self.is_valid(sudoku, row, col, nb):
                sudoku[row][col] = nb

                # Solver finish
                if self.solve_sudoku(sudoku):
                    self.result = True
                    self.end_time = time.time()
                    self.elapsed_time = self.end_time - self.start_time
                    # print(self.elapsed_time)
                    return self.elapsed_time,True
                
                # Return back
                sudoku[row][col] = '_'
        return False

    def run_solver(self, filename):
        sudoku = self.read_file(filename)
        if self.solve_sudoku(sudoku):
            self.result = True
            self.save_change('sudoku_solution.txt', sudoku)
        
    def begin(self,filename):
        print()
        self.display_grid(filename)
        self.run_solver(filename)
        self.display_grid('sudoku_solution.txt')
        start_time = time.time()
        
        if self.result:
            end_time = time.time()
            self.elapsed_time = end_time - start_time
            print(f"Sudoku résolu avec succès en {self.elapsed_time * 1000:.2f} millisecondes !")
        else:
            print("Pas de solution trouvée.")
        # print("Time to solver :", self.elapsed_time, "seconds")
        print()
