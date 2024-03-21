import pygame
import sys
from IBacktracking import SudokuSolver
pygame.init()

class Screen(SudokuSolver):
    def __init__(self):
        SudokuSolver.__init__(self)
        self.width = 900
        self.height = 600
        self.Window = pygame.display.set_mode((self.width,self.height))
        
        self.grid_start_x = 360
        self.grid_start_y = 130
        self.grid_end_x = 805
        self.grid_end_y = 570
        self.grid_width = self.grid_end_x - self.grid_start_x
        self.grid_height = self.grid_end_y - self.grid_start_y
        self.white = (255, 255, 255)
        self.white_1 = (255, 243, 231)
        self.white_2 = (255,231,206)
        self.white_3 = (254, 125, 94)
        self.black = (0,0,0)
        self.clock = pygame.time.Clock()
        self.grid = self.read_file("input/sudoku.txt")
        self.font = pygame.font.SysFont("Themundayfreeversion-Regular.ttf", 40)
        pygame.display.set_caption("Sudoku")

    def rect_full_not_centered(self,color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),0, radius)
        return button

    def rect_border(self,color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),  thickness, radius)
        return button

    def text_not_align(self,font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)
        
    def is_mouse_over_button(self,button_rect):
            mouse_pos = pygame.mouse.get_pos()
            return button_rect.collidepoint(mouse_pos)
        
    def button_hover(self,name, x, y, width, height, color_full, color_border, color_hover, color_border_hover, text, font, text_color,text_size, thickness, radius): 

            name = pygame.Rect(x,y, width, height)

            if self.is_mouse_over_button(name):
                self.rect_full_not_centered(color_hover, x-5, y-5, width + 10, height + 10, radius)
                self.rect_border(color_border_hover, x-5, y-5, width + 10, height + 10, thickness, radius)
            else:
                self.rect_full_not_centered(color_full, x, y, width, height, radius)
                self.rect_border(color_border, x, y, width, height, thickness, radius)
            self.text_not_align(font, text_size, text, text_color,  x, y)

            return name
        
    def display_rect(self):
        self.Window.fill(self.white_1)
        # self.rect_full_not_centered(self.white,340,20,480,580,10)
        self.rect_full_not_centered(self.white_2,340,20,480,570,10)
        self.rect_full_not_centered(self.white,360,130,445,445,10)
        self.rect_border(self.white_3, 340,20,480,570, 2, 10)
        self.rect_border(self.black, 358,129,447,449, 7, 10)
        self.button_solver = self.button_hover("Button solver", 80, 310, 180, 60, self.white_3, self.white_3, self.white_3, self.white_3, "     SOLVER", "Themundayfreeversion-Regular.ttf", self.white,33, 0, 10)

            
    def display_text(self):
        self.text_not_align("Themundayfreeversion-Regular.ttf", 50, "SUDOKU", self.black, 80, 100)
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "SOLVER", self.black, 530, 80)
        self.text_not_align("Themundayfreeversion-Regular.ttf", 30, "BRUTE FORCE", self.black, 500, 40)
        
    def load_sudoku_grid(self, filename):
        grid = []
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip()
                grid.append(row)
        return grid

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
                    number = self.font.render(self.grid[i][j], True, (0, 0, 0))
                    self.Window.blit(number, (self.grid_start_x + j * cell_size + (cell_size // 2 - number.get_width() // 2),
                                               self.grid_start_y + i * cell_size + (cell_size // 2 - number.get_height() // 2)))
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.display_rect()
                self.display_line()
                self.display_text()
                self.display_number()
                self.begin(self.grid)
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == pygame.MOUSEBUTTONDOWN():
                #     if self.button_solver.collidepoint(event.pos):
                #             pass
            
            pygame.display.flip()

        pygame.quit()
        sys.exit()

interface = Screen()
interface.run()
