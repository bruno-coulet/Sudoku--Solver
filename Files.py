class Files:
    def read_file(self,filename):
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(line.strip())
                sudoku.append(row)
        return sudoku
    
    # Save the sudoku to a file
    def save_change(self, new_filename, sudoku):
        with open(new_filename, 'w') as file:
            for row in sudoku:
                row=str(row)
                file.write(''.join(row) + '\n')
