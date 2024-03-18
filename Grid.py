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
        # Initiate a 9x9 grid filled with zeros
        grid = [[0]*9 for _ in range(9)]
        # Iterates every line of the string
        for i, ligne in enumerate(text.split('\n')):
            #  Iterates every element of the line.
            for j, number in enumerate(ligne):
                if number.isdigit():
                    # assigns the number to the current position in the grid
                    grid[i][j] = int(number)
        return grid

    def display_grid(self):
        print()
        #  Iterates the lines of the grid (from 0 to 8 included) -> Horizontal separation
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            #  Iterates the colunns of the grid (from 0 to 8 included) -> Vertical separation
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                # display the numbera t the position (i, j) in the grid.
                print(self.grid[i][j], end=" ")
            # skips to next line
            print()
        print()


def main():
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
    solver = Grid(f"input/{file_name}.txt")
    solver.display_grid()

if __name__ == "__main__":
    main()
