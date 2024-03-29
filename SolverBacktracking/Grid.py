import os
class Grid:
    def __init__(self):
        # List of _
        self.underscore_coordinates = [] 

    def read_file(self,file_name):
        with open(os.path.join(file_name), 'r') as f:
            data = f.read()
        return self.convert_into_grid(data)

    def convert_into_grid(self, text):

        # Initiate a 9x9 grid 
        grid = [["_"]*9 for _ in range(9)]
        # Iterates every line of the string
        for i, ligne in enumerate(text.split('\n')):
            #  Iterates every element of the line.
            for j, number in enumerate(ligne):
                if number.isdigit():
                    grid[i][j] = str(number)
                # Add coordinates of '_'
                elif number == "_":
                    self.underscore_coordinates.append((i, j))
      
        return grid

    def return_grid(self,file_name):
        self.grid = self.read_file(file_name)
        print()
        #  Lines -> Horizontal separation
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            #  Colunns -> Vertical separation
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                # Display the number in the grid
                if self.grid[i][j] == "_":
                    print("\033[94m" + self.grid[i][j] + "\033[0m", end=" ")
                else:
                    print(self.grid[i][j], end=" ")

                return self.grid[i][j]
            print()
        print()

    def display_grid(self,file_name):
        self.grid = self.read_file(file_name)
        print()
        #  Lines -> Horizontal separation
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            #  Colunns -> Vertical separation
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                # Display the number in the grid
                if self.grid[i][j] == "_":
                    print("\033[94m" + self.grid[i][j] + "\033[0m", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
                # if self.grid[i][j] == "_":
                #     print("\033[94m" + self.grid[i][j] + "\033[0m", end=" ")
                # else:
                #     print("\033[94m" + self.grid[i][j] + "\033[0m" if (i, j) in self.underscore_coordinates else self.grid[i][j], end=" ")


                    
            print()
        print()