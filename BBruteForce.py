from BGrid import BGrid
import random
import time

class Random_fill_and_check(BGrid):
    def __init__(self, file_name):
        super().__init__(file_name)

    '''Replace the 0 with a random number between 1 and 9 (inclusive)'''
    def fill(self):
        #  Get the grid as a string (grid_str)
        grid_str = self.display_grid()
        # Convert the grid string into a list of lines
        lines = grid_str.strip().split("\n")
        # Replace 0s with random integers between 1 and 9 (inclusive)
        for i in range(len(lines)):
            lines[i] = "".join(str(random.randint(1, 9)) if char == "0" else char for char in lines[i])

        # Reconstruct the grid string with random integers
        random_grid_str = "\n".join(lines)
        return random_grid_str

    '''Check the result. Return False if there are duplicates'''
    def check(self):
        for i in range(9):
            # i = index of the grid rows
            # self.grid[i][j] = each element in the row
            row = [self.grid[i][j] for j in range(9)]
            # convert the list into a set
            # compare the length of the set with 9
            # If the length of the set is != 9, there is at least one duplicate in row i
            if len(set(row)) != 9:
                return False
            # self.grid[j][i] = each element in the column
            column = [self.grid[j][i] for j in range(9)]
            if len(set(column)) != 9:
                return False
            
        # Checking for duplicates in the regions
        for i in range(0, 9, 3):  # rows 0, 3, and 6
            for j in range(0, 9, 3):  # columns 0, 3, and 6
                region = []
                # Loop to add numbers from the region to a list
                for x in range(3):
                    for y in range(3):
                        region.append(self.grid[i + x][j + y])
                if len(set(region)) != 9:
                    return False  # There is a duplicate in the region

        return True  # No duplicates found in all rows and columns
    
    '''Check if there are any zeros'''
    def has_zeros(self):
        for row in self.grid:
            if 0 in row:
                return True
        return False


def main():
    # Ask the user to choose a Sudoku grid
    file_name = input("Entrez le nom du fichier contenant la grille de Sudoku : ")

    # Instantiate BGrid classes to load the grid
    grid = BGrid(f"input/{file_name}.txt")

    # Instantiate Random_fill_and_check to fill the grid
    random_fill_and_check = Random_fill_and_check(f"input/{file_name}.txt")

    # Display the original grid
    grid_display = grid.display_grid()
    print("Grille originale :\n")
    print(grid_display)

    # Start the timer
    start_time = time.time()

    # Loop while there are zeros in the grid
    while random_fill_and_check.has_zeros():
        # Fill the grid with random integers
        random_grid_str = random_fill_and_check.fill()

        # Check the result. Duplicates => False, No duplicate => True
        if random_fill_and_check.check():
            # Display the filled grid
            print("Grille remplie avec des entiers aléatoires :\n")
            print(random_grid_str)
            break
        else:
            print("Il y a un doublon ou plus. Regénération de la grille...")

    # Stop the timer
    end_time = time.time()
    solver_time = end_time - start_time
    print(f'\nTemps d\'éxecution : {solver_time}\n')


if __name__ == "__main__":
    main()