class Files:
    
    def read_file(self,filename):
        # Read the file and add each line to the list
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(line.strip())
                sudoku.append(row)
        return sudoku
    
    def save_change(self, new_filename, sudoku):
        # Save the list into a file
        with open(new_filename, 'w') as file:
            for row in sudoku:
                file.write(''.join(row) + '\n')

