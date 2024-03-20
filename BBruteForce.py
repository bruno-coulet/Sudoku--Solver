from BGrid import BGrid
import random

class Random(BGrid):
    def __init__(self, file_name):
        super().__init__(file_name)

    '''Remplace les 0 par un chiffre aléatoire entre 1 et 9 inclus'''
    def generate_random_sudoku(self):
        # Obtient la grille sous forme de chaîne de caractères (grid_str)
        grid_str = self.display_grid()
        # Convertit la chaîne de grille en une liste de lignes
        lines = grid_str.strip().split("\n")
        # Remplace les zéros par des entiers aléatoires entre 1 et 9 inclus
        for i in range(len(lines)):
            lines[i] = "".join(str(random.randint(1, 9)) if char == "0" else char for char in lines[i])

        # Reconstruit la chaîne de grille avec les entiers aléatoires
        random_grid_str = "\n".join(lines)
        return random_grid_str

    def check(self):
        for i in range(9):
            # i = indice des lignes de la grille
            # self.grid[i][j] = chaque élément de la ligne
            row = [self.grid[i][j] for j in range(9)]
            # converti la liste en un ensemble (set)
            # comparant la longueur de l'ensemble avec 9
            # Si la longueur de l'ensemble est != 9, il y a au moins un doublon dans la ligne i
            if len(set(row)) != 9:
                return False
            # self.grid[j][i] = chaque élément de la colonne
            column = [self.grid[j][i] for j in range(9)]
            if len(set(column)) != 9:
                return False
            
        # Vérification des doublons dans les régions
        for i in range(0, 9, 3):  # lignes 0, 3 et 6
            for j in range(0, 9, 3):  # colonnes 0, 3 et 6
                region = []
                # Boucle pour ajouter les nombres de la région à une liste
                for x in range(3):
                    for y in range(3):
                        region.append(self.grid[i + x][j + y])
                if len(set(region)) != 9:
                    return False  # Il y a un doublon dans la région

        return True  # Aucun doublon trouvé dans toutes les lignes et colonnes


def main():
    # Instancie la classe Random
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
    generator = Random(f"input/{file_name}.txt")
    grid = BGrid(f"input/{file_name}.txt")

    # Affiche la grille originale
    grid_display = grid.display_grid()
    print("Grille originale :\n")
    print(grid_display)

    # # Génère une nouvelle grille avec des entiers aléatoires
    # random_grid_str = generator.generate_random_sudoku()

    # # Affiche la grille remplie
    # print("Grille remplie avec des entiers aléatoires :\n")
    # print(random_grid_str)


    while True:
        # Génère une nouvelle grille avec des entiers aléatoires
        random_grid_str = generator.generate_random_sudoku()

        # Vérifie s'il y a un doublon dans chaque ligne ou colonne
        if generator.check():
            break
        else:
            print("Doublon trouvé dans au moins une ligne ou colonne. Regénération de la grille...")

    # Affiche la grille remplie
    print("Grille remplie avec des entiers aléatoires :\n")
    print(random_grid_str)

if __name__ == "__main__":
    main()
