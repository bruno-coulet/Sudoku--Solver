import os
class Grid:
    def __init__(self):
        pass
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
        return grid

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
                print(self.grid[i][j], end=" ")
            print()
        print()
        