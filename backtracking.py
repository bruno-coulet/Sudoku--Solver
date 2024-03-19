import os

# The Grid class represents a Sudoku grid.
class Grid:
    def __init__(self):
        pass

    # This method reads a file from the 'input' directory and returns its content as a grid.
    def read_file(self, file_name):
        with open(os.path.join('input', file_name), 'r') as f:
            data = f.read()
        return self.convert_into_grid(data)

    # This method converts a text representation of a Sudoku grid into a 2D list.
    def convert_into_grid(self, text):
        grid = [[0]*9 for _ in range(9)] 
        for i, line in enumerate(text.split('\n')):
            for j, number in enumerate(line):
                if number.isdigit():
                    grid[i][j] = int(number)  
        return grid

    # This method displays a Sudoku grid.
    def display_grid(self, grid):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('-'*21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print('|', end='')
                print(grid[i][j], end=' ')
            print()

# The Solver class is used to solve a Sudoku puzzle.
class Solver(Grid):
    def __init__(self):
        Grid.__init__(self)

    # This method checks if a number can be placed in a specific spot on the grid.
    def is_valid(self, sudoku, row, col, num):
        for x in range(9):
            if sudoku[row][x] == num:
                return False
            if sudoku[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if sudoku[i + start_row][j + start_col] == num:
                    return False
        return True

    # This method solves the Sudoku puzzle using backtracking.
    def solve(self, sudoku, row=0, col=0):
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if sudoku[row][col] > 0:
            return self.solve(sudoku, row, col + 1)
        for num in range(1, 10):
            if self.is_valid(sudoku, row, col, num):
                sudoku[row][col] = num
                if self.solve(sudoku, row, col + 1):
                    return True
            sudoku[row][col] = 0
        return False

    # This method starts the solving process.
    def begin(self):
        self.file_name = input("Entrez le nom du fichier contenant la grille de Sudoku :")
        sudoku = self.read_file(f"{self.file_name}.txt")
        self.display_grid(sudoku)
        if self.solve(sudoku):
            print("Sudoku résolu avec succès !")
            self.display_grid(sudoku)
        else:
            print("Pas de solution trouvée.")

# Create a Solver object and start the solving process.
solver = Solver()
solver.begin()
