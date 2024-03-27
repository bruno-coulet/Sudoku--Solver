from Grid import Grid
import time

# The Solver class is used to solve a Sudoku puzzle.
class Solver(Grid):
    def __init__(self):
        Grid.__init__(self)

    # This method checks if a number can be placed in a specific spot on the grid.
    def is_valid(self, sudoku, row, col, num):
    # Check if 'num' is already in the current row
        for x in range(9):
            if sudoku[row][x] == num:
                return False

    # Check if 'num' is already in the current column
        for x in range(9):
            if sudoku[x][col] == num:
                return False

    # Trouvez le début de la rangée et de la colonne pour la boîte 3x3 actuelle
            start_row = row - row % 3
            start_col = col - col % 3

    # Iterate through each cell of the current 3x3 box
        for i in range(3):
            for j in range(3):
            # If 'num' is found, return False
                if sudoku[i + start_row][j + start_col] == num:
                    return False

    # If 'num' is not found in the row, column, and 3x3 box, return True
        return True

    # This method solves the Sudoku puzzle using backtracking.
    def solve(self, sudoku, row=0, col=0):
        # If we've reached the 9th column of the 8th row, we've filled the Sudoku correctly
            if row == 8 and col == 9:
                return True

        # If the column is 9, we've reached the end of the row,
        # so we move to the next row and reset the column to 0
            if col == 9:
                row += 1
                col = 0

            # If the current cell already has a value, move to the next cell
            if sudoku[row][col] > 0:
                return self.solve(sudoku, row, col + 1)

            # Si la cellule actuelle est vide, essayez chaque nombre de 1 à 9
            for num in range(1, 10):
            # Vérifiez si le numéro est valide pour la cellule actuelle
                if self.is_valid(sudoku, row, col, num):
                # Si le numéro est valide, placez-le dans la cellule actuelle
                    sudoku[row][col] = num

                # Passez à la cellule suivante et si la solution est trouvée, retournez True
                    if self.solve(sudoku, row, col + 1):
                        return True

            # If no number is valid or if the solution is not found, backtrack and try the next number
            sudoku[row][col] = 0

            #  If no number can be placed in the current cell, return False
            return False

    # This method starts the solving process.
    def begin(self, algo_name, file_name):

        # self.file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
        sudoku = self.read_file(file_name)
        print ("\nGrille originale")
        self.display_grid(sudoku)

        start_time = time.time()

        if self.solve(sudoku):
            print ("Grille résolue")
            self.display_grid(sudoku)
            end_time = time.time()
            total_time = end_time - start_time
            print(f"{file_name} résolu avec succès en {(total_time) * 1000:.2f} millisecondes !\n")

            
            return total_time
        
        else:
            print("Pas de solution trouvée.")
            return None


# Create a Solver object and start the solving process.
# solver = Solver()
# solver.begin()
