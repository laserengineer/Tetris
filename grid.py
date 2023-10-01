import pygame
from colors import Colors
class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # list of lists for each cell
        self.colors = Colors.get_cell_colors()
    
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column],end = " ")
            print()
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Rect (x,y,w,h), x and y coordinate of its top left corner , its width and its height
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1 )
                # pygame.draw.rect(surface, color, rect )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
        