class Grid:
    def __init__(self, file_name):
        self.file_name = file_name
        self.grid = self.read_file()

    def read_file(self):
        with open(self.file_name, 'r') as f:
            data = f.read()
        return self.convert_into_grid(data)

    '''Converti le fichier .txt en chaine de caractères
    arg : str
    returns : la grille (liste de listes)
    '''
    def convert_into_grid(self, text):
        # Initialisation d'une grille 9x9 remplie de zéros.
        grid = [[0]*9 for _ in range(9)]
        # Itération sur chaque ligne de la chaîne de texte après l'avoir divisée par le saut de ligne.
        for i, ligne in enumerate(text.split('\n')):
            #  Itération sur chaque caractère de la ligne.
            for j, number in enumerate(ligne):
                if number.isdigit():
                    # assignation à la position correspondante dans la grille.
                    grid[i][j] = int(number)
        return grid

    def display_grid(self):
        print()
        #  Itération sur les lignes de la grille (de 0 à 8 inclus) -> Séparation horizontale
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            #  Itération sur les colonnes de la grille (de 0 à 8 inclus) -> Séparation verticale
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                # Affichage du nombre situé à la position (i, j) de la grille.
                print(self.grid[i][j], end=" ")
            # Passe à la ligne suivante
            print()
        print()


def main():
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
    solver = Grid(f"input/{file_name}.txt")
    solver.display_grid()

if __name__ == "__main__":
    main()
