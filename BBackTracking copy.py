from BGrid import BGrid

class BBackTracking(BGrid):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.solution = None

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Toutes les cellules sont remplies, le Sudoku est résolu

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num

                if self.solve_sudoku():
                    return True  # Récursion pour résoudre le reste du Sudoku

                # Si la valeur actuelle ne mène pas à une solution, la remettre à 0
                self.grid[row][col] = 0

        return False  # Aucune valeur n'a mené à une solution, donc revenir en arrière

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None  # Aucune cellule vide trouvée

    def is_valid_move(self, row, col, num):
        # Vérifie la validité du numéro dans la ligne
        if num in self.grid[row]:
            return False

        # Vérifie la validité du numéro dans la colonne
        if num in [self.grid[i][col] for i in range(9)]:
            return False

        # Vérifie la validité du numéro dans le carré 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def display_solution(self):
        if self.solution:
            return self.solution
        else:
            self.solve_sudoku()
            self.solution = self.display_grid()
            return self.solution


def main():
    # Instancie la classe SudokuSolver
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
    solver = BBackTracking(f"input/{file_name}.txt")

    # Affiche la grille originale
    grid_display = solver.display_grid()
    print("Grille originale :\n")
    print(grid_display)

    # Résout le Sudoku
    print("\nRésolution du Sudoku :")
    solution = solver.display_solution()
    print(solution)

if __name__ == "__main__":
    main()
