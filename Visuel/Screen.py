import pygame
import time
import sys
from Solver.Backtracking import Backtracking
from Visuel.Element import Element
pygame.init()

class Screen(Backtracking,Element):
    def __init__(self):
        Backtracking.__init__(self)
        Element.__init__(self)

        self.start_time = 0
        self.research = False
        self.grid_start_x = 360
        self.grid_start_y = 130
        self.grid_end_x = 805
        self.grid_end_y = 570
        self.grid_width = self.grid_end_x - self.grid_start_x
        self.grid_height = self.grid_end_y - self.grid_start_y

        # self.result = False
        self.clock = pygame.time.Clock()
        self.file = "input/sudoku.txt"
        self.elapsed_time = 0
        self.grid = self.read_file(self.file)
        self.font = pygame.font.SysFont("Themundayfreeversion-Regular.ttf", 40)
        pygame.display.set_caption("Sudoku")


        
    def display_rect(self):
        self.Window.fill(self.white_1)
        self.rect_full_not_centered(self.white_2,340,20,480,570,10)
        self.rect_full_not_centered(self.white,360,130,445,445,10)
        self.rect_border(self.white_3, 340,20,480,570, 2, 10)
        self.rect_border(self.black, 358,129,447,449, 7, 10)
        self.button_solver = self.button_hover("Button solver", 80, 310, 180, 60, self.white_3, self.white_3, self.white_3, self.white_3, "    SOLVER", "Themundayfreeversion-Regular.ttf", self.white,33, 0, 10)
        
        self.rect_full_not_centered(self.white,40,50,270,50,10)
        
        self.sudoku_1 = self.button_hover("sudoku_1", 50, 55, 40, 40, self.white_1, self.white_1, self.white_1,self.white_1, " 1", "Themundayfreeversion-Regular.ttf", self.white_5,33, 0, 10)
        self.sudoku_2 = self.button_hover("sudoku_2", 100, 55, 40, 40, self.white_2, self.white_2, self.white_2, self.white_2, " 2", "Themundayfreeversion-Regular.ttf", self.white_4,33, 0, 10)
        self.sudoku_3 = self.button_hover("sudoku_3", 150, 55, 40, 40, self.white_3, self.white_3, self.white_3, self.white_3, " 3", "Themundayfreeversion-Regular.ttf", self.black,33, 0, 10)
        self.sudoku_4 = self.button_hover("sudoku_4", 200, 55, 40, 40, self.white_4, self.white_4, self.white_4, self.white_4, " 4", "Themundayfreeversion-Regular.ttf", self.white_3,33, 0, 10)
        self.sudoku_5 = self.button_hover("sudoku_5", 255, 55, 40, 40, self.white_5, self.white_5, self.white_5, self.white_5, " 5", "Themundayfreeversion-Regular.ttf", self.white_1,33, 0, 10)
        
    def display_text(self):
        self.text_not_align("Themundayfreeversion-Regular.ttf", 50, "SUDOKU", self.black, 80, 100)
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "SOLVER", self.black, 530, 80)
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "BACKTRACKING", self.black, 500, 40)



    def display_line(self):
        cell_size = self.grid_width // 9
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.Window, (0, 0, 0), (self.grid_start_x + i * cell_size, self.grid_start_y), 
                             (self.grid_start_x + i * cell_size, self.grid_end_y), thickness)
            pygame.draw.line(self.Window, (0, 0, 0), (self.grid_start_x, self.grid_start_y + i * cell_size), 
                             (self.grid_end_x, self.grid_start_y + i * cell_size), thickness)

    def display_number(self):
        cell_size = self.grid_width // 9
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != '_':
                    number = self.font.render(str(self.grid[i][j]), True, self.black)
                    self.Window.blit(number, (self.grid_start_x + j * cell_size + (cell_size // 2 - number.get_width() // 2),
                                               self.grid_start_y + i * cell_size + (cell_size // 2 - number.get_height() // 2)))

    def display_result(self):
        if self.research:
            if self.result==True:
                self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "Sodoku Finish", self.black, 70, 500)
            else: 
                self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "In progress...", self.black, 70, 500)
        else: 
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "Sudoku empty", self.black, 70, 500)

    def display_time(self, time):
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "Time :", self.black, 70, 400)

        if self.start_time != 0:
            time_str = "{:.10f}".format(time)
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, time_str[:6], self.black, 80, 440)
        else:
            self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "0", self.black, 80, 440)
            
    def load_sudoku_grid(self, filename):
        grid = []
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip()
                grid.append(row)
        return grid
    
    def run(self):        
        running = True                         
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sudoku_1.collidepoint(event.pos):
                        self.file = "input/sudoku.txt"
                        self.return_grid(self.file)
                        self.display_number()
                        
                    elif self.sudoku_2.collidepoint(event.pos):
                        self.file = "input/sudoku2.txt"
                        self.return_grid(self.file)
                        self.display_number()
                        
                    elif self.sudoku_3.collidepoint(event.pos):
                        self.file = "input/sudoku3.txt"
                        self.return_grid(self.file)
                        self.display_number()
                        
                    elif self.sudoku_4.collidepoint(event.pos):
                        self.file = "input/sudoku4.txt"
                        self.return_grid(self.file)
                        self.display_number()
                        
                    elif self.sudoku_5.collidepoint(event.pos):
                        self.file = "input/evilsudoku.txt"
                        self.return_grid(self.file)
                        self.display_number()
                        
                    elif self.button_solver.collidepoint(event.pos):
                        self.research = True
                        if self.research:
                            self.begin(self.file)
                            self.grid = self.load_sudoku_grid("sudoku_solution.txt")
                            self.display_number()
                            if self.result == True:
                                self.display_time(self.elapsed_time)

            self.display_rect()
            self.display_line()
            self.display_text()
            self.display_number()
            self.display_result()
            self.display_time(self.elapsed_time)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

# interface = Screen()
# interface.run()