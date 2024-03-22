from Grid import Grid
import time

# The Solver class is used to solve a Sudoku puzzle.
class Solver(Grid):
    def __init__(self):
        Grid.__init__(self)

    # This method checks if a number can be placed in a specific spot on the grid.
    def is_valid(self, sudoku, row, col, num):
    # Vérifiez si 'num' est déjà dans la ligne actuelle
        for x in range(9):
            if sudoku[row][x] == num:
                return False

    # Vérifiez si 'num' est déjà dans la colonne actuelle
        for x in range(9):
            if sudoku[x][col] == num:
                return False

    # Vérifiez si 'num' est déjà dans la boîte 3x3 actuelle
    # Trouvez le début de la rangée et de la colonne pour la boîte 3x3 actuelle
            start_row = row - row % 3
            start_col = col - col % 3

    # Parcourez chaque cellule de la boîte 3x3
        for i in range(3):
            for j in range(3):
            # Si 'num' est trouvé, retournez False
                if sudoku[i + start_row][j + start_col] == num:
                    return False

    # Si 'num' n'est pas trouvé dans la ligne, la colonne et la boîte 3x3, retournez True
        return True

    # This method solves the Sudoku puzzle using backtracking.
    def solve(self, sudoku, row=0, col=0):
        # Si nous avons atteint la 9ème colonne de la 8ème ligne, nous avons rempli le Sudoku correctement
            if row == 8 and col == 9:
                return True

        # Si la colonne est 9, nous avons atteint la fin de la ligne,
        # donc nous passons à la ligne suivante et réinitialisons la colonne à 0
            if col == 9:
                row += 1
                col = 0

        # Si la cellule actuelle a déjà une valeur, passez à la cellule suivante
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

            # Si aucun numéro n'est valide ou si la solution n'est pas trouvée, annulez le choix (backtrack) et essayez le prochain numéro
                sudoku[row][col] = 0

        # Si aucun numéro ne peut être placé dans la cellule actuelle, retournez False
            return False

    # This method starts the solving process.
    def begin(self):

        self.file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")

        # Start the timer
        start_time = time.time()

        sudoku = self.read_file(f"{self.file_name}.txt")
        self.display_grid(sudoku)

        start_time = time.time()

        if self.solve(sudoku):
            end_time = time.time()
            print(f"Sudoku résolu avec succès en {end_time - start_time} secondes !")
            self.display_grid(sudoku)
        else:
            print("Pas de solution trouvée.")

        # Stop the timer
        end_time = time.time()
        solver_time = (end_time - start_time) *1000
        print(f'\nTemps d\'éxecution : {solver_time:.2f} millisecondes\n')


# Create a Solver object and start the solving process.
solver = Solver()
solver.begin()
