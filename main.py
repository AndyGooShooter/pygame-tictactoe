### IMPORTS (libraries and functions from other files)
import pygame
import settings
from utility_functions import render
from utility_functions import legal_move
from utility_functions import make_move



### GAME CONFIGURATION
pygame.init()
screen = pygame.display.set_mode((settings.master_h, settings.master_w))
turn = 0 # turn counter, starts with 0
         # even numbers are white, odd numbers are black
running = True  
         
         
         
### ASSETS
bg = pygame.image.load("Assets/bg.png")
white_point = pygame.image.load("Assets/white_point.png")
black_point = pygame.image.load("Assets/black_point.png")

bg = pygame.transform.scale(bg, (settings.master_h, settings.master_w))
white_point = pygame.transform.scale(white_point, (settings.master_point_h, settings.master_point_w))
black_point = pygame.transform.scale(black_point, (settings.master_point_h, settings.master_point_w))



### GAME LOOP
while running: # basically runs forever unless we tell it to stop
    screen.blit(bg, (0, 0)) 
    
    for event in pygame.event.get(): # here we check everything that happens in the game
                                     # those are called events and there are multiple kinds
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            click_row = int((mouse_x + settings.master_offset) / settings.master_square_w)
            click_col = int((mouse_y + settings.master_offset) / settings.master_square_h)
            player = turn % 2 + 1 # player = 1 is white, player = 2 is black
            
            if legal_move(click_row, click_col):
                turn += 1
                make_move(click_row, click_col, player) # making the move in the array (backend)
                print("Row: " + str(click_row) + ", Col: " + str(click_col))

            else:
                print("Illegal move")
            
        if event.type == pygame.QUIT:
            running = False
            
            
    render(screen, white_point, black_point) # rendering the move on the screen (frontend)
    pygame.display.update() # update the display with all the .blit() changes 

pygame.quit()