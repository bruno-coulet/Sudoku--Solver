import os
from SudokuSolver import SudokuSolver

class BruteForce(SudokuSolver):
    def __init__(self):
        SudokuSolver.__init__(self)

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
    
    def again(self):
        print("ok")
        self.run()
        
brute_force = BruteForce()
filename = 'sudoku_random_generated.txt'
sudoku = brute_force.read_sudoku(filename)

if brute_force.verification(sudoku):
    print("Good grid")
else:
    nom_fichier = "sudoku_random_generated.txt"

    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
    # brute_force.run()
    print("Bad grid")

