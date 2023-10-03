import pygame, sys
from game import Game
from colors import Colors


# Initialize the game
pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)



# Set game window display canvas size 300 * 600
screen = pygame.display.set_mode((500, 620) )  
pygame.display.set_caption("Python Tetris")


clock = pygame.time.Clock()
game = Game()

Game_Update = pygame.USEREVENT
pygame.time.set_timer(Game_Update, 200)

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
                game.game_over = False
                game.reset()                
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)               
                
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        
        if event.type == Game_Update and game.game_over == False:
            game.move_down()
            
                
                
            

    # Drawing
    # The background is dark_blue, the rect is dark_grey
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    # Create grid of 10 columns and 20 rows , the game pieces call tetrominoes

    # Updating Positions
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
    # Drawing Objects
