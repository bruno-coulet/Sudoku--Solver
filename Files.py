class Files:
    
    def read_file(self,filename):
        sudoku = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(line.strip())
                sudoku.append(row)
        return sudoku
    
    def save_change(self, new_filename, sudoku):
        with open(new_filename, 'w') as file:
            for row in sudoku:
                file.write(''.join(row) + '\n')
                
    # def run_solver(self, filename):

    #     sudoku = self.read_file(filename)
    #     if self.solve_sudoku(sudoku):
    #         # self.save_change('sudoku_solution.txt', sudoku)
    #         self.save_change('sudoku_solution.txt', sudoku)

                
