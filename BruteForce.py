# import os
from SudokuSolver import SudokuSolver
from Grid import Grid
import time

class BruteForce(SudokuSolver,Grid):
    def __init__(self):
        SudokuSolver.__init__(self)
        Grid.__init__(self)
        self.result = False

    def verification(self,sudoku):
        # Check
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                
                # Check row
                if sudoku[i][j] != '_':
                    if sudoku[i][j] in row:
                        return False
                    row.add(sudoku[i][j])
                    
                # Check column
                if sudoku[j][i] != '_':
                    if sudoku[j][i] in col:
                        return False
                    col.add(sudoku[j][i])

        # Check 3x3 
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                region_nums = set()
                for k in range(3):
                    for l in range(3):
                        if sudoku[i+k][j+l] != '_':
                            if sudoku[i+k][j+l] in region_nums:
                                return False
                            region_nums.add(sudoku[i+k][j+l])
        return True
    
    def read_sudoku(self,file_name):
        sudoku = []
        with open(file_name, 'r') as file:
            for line in file:
                row = [char for char in line.strip()]
                sudoku.append(row)
        return sudoku

    def begin(self, file_name):
        # new_file_name = 'SudokuBruteForce.txt'
        # self.run_solver(file_name)
        # self.display_grid(new_file_name)
        # sudoku = self.read_sudoku(new_file_name)
        # self.result = bool(self.verification(sudoku))
        sudoku = self.read_sudoku(file_name)

        start_time = time.time()

        if self.run_solver(sudoku):
            print ("Grille résolue")
            self.display_grid(sudoku)
            end_time = time.time()
            total_time = end_time - start_time
            print(f"{file_name} résolu avec succès en {(total_time) * 1000:.2f} millisecondes !\n")

            
            return total_time
        
        else:
            print("Pas de solution trouvée.")
            return None

        