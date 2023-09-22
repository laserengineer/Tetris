import pygame
class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # list of lists for each cell
        self.colors = self.get_cell_colors()
    
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column],end = " ")
            print()
    
    def get_cell_colors(self):        
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (266, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Rect (x,y,w,h), x and y coordinate of its top left corner , its width and its height
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1 )
                # pygame.draw.rect(surface, color, rect )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
        