import os
from SudokuSolver import SudokuSolver
from Grid import Grid

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
    
    def read_sudoku(self,filename):
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = [char for char in line.strip()]
                sudoku.append(row)
        return sudoku

    # def begin(self):
    #     new_filename = 'SudokuBruteForce.txt'
    #     self.file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
    #     self.display_grid(f"input/{self.file_name}.txt")
    #     self.run_solver(f"input/{self.file_name}.txt")
    #     self.display_grid(new_filename)
    #     sudoku = self.read_sudoku(new_filename)
    #     if self.verification(sudoku):
    #         print("Good grid")
    #     else:
    #         file_remove = "SudokuBruteForce.txt"

    #         if os.path.exists(file_remove):
    #             os.remove(file_remove)
    #         print("Bad grid")



    def begin(self,filename):
        new_filename = 'SudokuBruteForce.txt'
        self.run_solver(filename)
        self.display_grid(new_filename)
        sudoku = self.read_sudoku(new_filename)
        self.result = bool(self.verification(sudoku))

        