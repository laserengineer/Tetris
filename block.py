from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        # Store the occupied cells in the bounding grid 
        # for each rotation state of the block     
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns 
    
    def get_cell_positions(self):
        # Tiles is used for actual positions shown to user 
        # It is one key instance for  
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0 

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1          

    
    def draw(self,screen):
    # need to know the surface and position to draw
        tiles = self.get_cell_positions() # tiles is a Position Objects list 
        for tile in tiles: # tile is Position object instance 
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
    
        
         
   