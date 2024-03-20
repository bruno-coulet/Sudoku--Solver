import os
from SudokuSolver import SudokuSolver
from Grid import Grid

class BruteForce(SudokuSolver,Grid):
    def __init__(self):
        SudokuSolver.__init__(self)
        Grid.__init__(self)

    def verification(self,sudoku):
        # Vérification des lignes et des colonnes
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                
                # Vérification des lignes
                if sudoku[i][j] != '_':
                    if sudoku[i][j] in row:
                        return False
                    row.add(sudoku[i][j])
                    
                # Vérification des colonnes
                if sudoku[j][i] != '_':
                    if sudoku[j][i] in col:
                        return False
                    col.add(sudoku[j][i])

        # Vérification des régions
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
        # sourcery skip: identity-comprehension
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = [char for char in line.strip()]
                sudoku.append(row)
        return sudoku

    def begin(self):
        new_filename = 'sudoku_random_generated.txt'
        self.file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
        self.display_grid(f"input/{self.file_name}.txt")
        self.run_solver(f"input/{self.file_name}.txt")
        self.display_grid(new_filename)
        sudoku = self.read_sudoku(new_filename)
        if self.verification(sudoku):
            print("Good grid")
        else:
            file_remove = "sudoku_random_generated.txt"

            if os.path.exists(file_remove):
                os.remove(file_remove)
            print("Bad grid")




