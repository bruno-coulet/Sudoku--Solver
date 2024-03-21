class Files:

    def read_file(filename):
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(line.strip())
                sudoku.append(row)
        return sudoku

    def save_change(new_filename, sudoku):
        with open(new_filename, 'w') as file:
            for row in sudoku:
                file.write(''.join(row) + '\n')

    
    