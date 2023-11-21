### IMPORTS (libraries and functions from other files)
import pygame
import settings
from utility_functions import render, is_legal_move, make_move, check_win

### GAME CONFIGURATION
pygame.init()
screen = pygame.display.set_mode((settings.master_w, settings.master_h))
turn = 0 # turn counter, starts with 0
         # even numbers are white, odd numbers are black

### ASSETS
bg = pygame.image.load("assets/bg.png")
white_point = pygame.image.load("assets/white_point.png")
black_point = pygame.image.load("assets/black_point.png")

bg = pygame.transform.scale(bg, (settings.master_w, settings.master_h))
white_point = pygame.transform.scale(white_point, (settings.master_point_w, settings.master_point_h))
black_point = pygame.transform.scale(black_point, (settings.master_point_w, settings.master_point_h))

### INITIALISE BOARD ARRAY
board = [
    [-1, -1, -1, -1, -1, -1, -1, -1], # row 0
    
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 1
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 2
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 3
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 4
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 5
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 6
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 7
    [-1,     0, 0, 0, 0, 0, 0, 0, 0], # row 8
]
winner = -1
running = True

### GAME LOOP
while running: # basically runs forever unless we tell it to stop
    screen.blit(bg, (0, 0)) 
    
    for event in pygame.event.get(): # here we check everything that happens in the game
                                     # those are called events and there are multiple kinds
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            click_row = int((mouse_x + settings.master_offset) / settings.master_square_h)
            click_col = int((mouse_y + settings.master_offset) / settings.master_square_w)
            
            if is_legal_move(board, click_row, click_col):
                player = turn % 2 + 1 # player = 1 is white, player = 2 is black
                turn += 1
                make_move(board, click_row, click_col, player) # making the move in the array (backend)
                print("Row: " + str(click_row) + ", Col: " + str(click_col))
                winner = check_win(board)
                if winner != -1:
                    running = False
                    print(f'Player {winner} has won!')

            else:
                print("Illegal move")
            
        if event.type == pygame.QUIT:
            running = False
            
    text = pygame.font.Font('assets/font.otf', 32).render("Turn: " + str(turn), True, (255, 255, 255))
    screen.blit(text, (settings.master_text_w, settings.master_text_h))
    render(screen, board, white_point, black_point) # rendering the move on the screen (frontend)
    pygame.display.update() # update the display with all the .blit() changes 

pygame.quit()