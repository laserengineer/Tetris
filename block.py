from colors import Colors
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {} # Store the occupied cells in the bounding grid for each rotation state of the block
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    def draw(self,screen):
    # need to know the surface and position to draw
        tiles = self.cells[self.rotation_state] # tiles is a Position Objects list 
        for tile in tiles: # tile is Position object instance 
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
    
        
         
 