import pygame, sys
from game import Game

# Initialize the game
pygame.init()
dark_blue = (44, 44, 127)

# Set game window display canvas size 300 * 600
screen = pygame.display.set_mode((300, 600) )  
pygame.display.set_caption("Python Tetris")


clock = pygame.time.Clock()
game = Game()

Game_Update = pygame.USEREVENT
pygame.time.set_timer(Game_Update, 20)

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
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over == False
                game.reset()                
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        
        if event.type == Game_Update and game.game_over == False:
            game.move_down()
            
                
                
            

    # Drawing
    # The background is dark_blue, the rect is dark_grey
    screen.fill(dark_blue)
    game.draw(screen) 

    # Create grid of 10 columns and 20 rows , the game pieces call tetrominoes

    # Updating Positions
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
    # Drawing Objects
