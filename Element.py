import pygame
class Element:
    def __init__(self):
        # Window
        self.width = 900
        self.height = 600
        self.Window = pygame.display.set_mode((self.width,self.height))
        
        # Color
        self.white = (255, 255, 255)
        self.white_1 = (255, 243, 231)
        self.white_2 = (255,231,206)
        self.white_3 = (254, 125, 94)
        self.black = (0,0,0)
     
    # Display rectangle full
    def rect_full_not_centered(self,color, x, y, width, height, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),0, radius)
        return button

    # Display rectangle border
    def rect_border(self,color, x, y, width, height, thickness, radius):
        button = pygame.draw.rect(self.Window, color, pygame.Rect(x, y, width, height),  thickness, radius)
        return button

    # Display text
    def text_not_align(self,font, text_size, text_content, color, x, y):
        text = pygame.font.Font(f"{font}", text_size).render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Window.blit(text, text_rect)
    
    # Event mouse click
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