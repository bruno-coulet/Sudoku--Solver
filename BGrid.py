class BGrid:
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
        grid_str = ""
        #  Iterates the lines of the grid (from 0 to 8 included) -> Horizontal separation
        for i in range(9):
            if i % 3 == 0 and i != 0:
                grid_str += "-" * 21 + "\n"
            #  Iterates the colunns of the grid (from 0 to 8 included) -> Vertical separation
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    grid_str += "| "
                # display the number at the position (i, j) in the grid.
                grid_str += str(self.grid[i][j]) + " "
            # skips to next line
            grid_str += "\n"
        return grid_str


def main():
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
    grid = BGrid(f"input/{file_name}.txt")
    grid_display = grid.display_grid()
    print(grid_display)


    return grid_display

if __name__ == "__main__":
    main()
