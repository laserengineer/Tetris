import pygame, sys
from grid import Grid

# Initialize the game 
pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) # Set game window display canvas size 300 * 600
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
game_grid = Grid()
game_grid.print_grid()
# game frame per second 

# Game Loop 
# 1. Event Handling 
# 2. Updating Positions
# 3. Drawing Objects 

while True:
    
    # Checking for Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)

    # Create grid of 10 columns and 20 rows , the game pieces call tetrominoes 
        
    # Updating Positions 
    pygame.display.update()
    clock.tick(60) # 60 frames per second 
    # Drawing Objects 