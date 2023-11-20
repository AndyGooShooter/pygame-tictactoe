### IMPORTS (libraries and functions from other files)
import pygame
import settings as s

### GAME CONFIGURATION
pygame.init()
screen = pygame.display.set_mode((s.master_h, s.master_w))
turn = 0 # turn counter, starts with 0
         # even numbers are white, odd numbers are black
# assets
bg = pygame.image.load("Assets/bg.png")
white_point = pygame.image.load("Assets/white_point.png")
black_point = pygame.image.load("Assets/black_point.png")

bg = pygame.transform.scale(bg, (s.master_h, s.master_w))
white_point = pygame.transform.scale(white_point, (s.master_h, s.master_w))
black_point = pygame.transform.scale(black_point, (s.master_h, s.master_w))

# the array
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



### GAME LOOP
while True: # basically runs forever unless we tell it to stop
    screen.blit(bg, (0, 0)) 
    
    for event in pygame.event.get(): # here we check everything that happens in the game
                                     # those are called events and there are multiple kinds
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click_row = int((mouse_x - master_offset) / master_square_w) + 1
            click_col = int((mouse_y - master_offset) / master_square_h) + 1
            
            print("Row: " + str(click_row) + ", Col: " + str(click_col))
            
            
            player = turn % 2 # 0 is white, 1 is black
            
            board[click_col][click_row] = player # making the move in the array
            
            # getting coordinates for the point
            build_x = master_offset + (click_row - 1) * master_square_w 
            build_y = master_offset + (click_col - 1) * master_square_h
   
            if player == 0: # making the move on the display
                screen.blit(white_point, (build_x, build_y))
            else:
                screen.blit(black_point, (build_x, build_y))
            
            turn += 1
            
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.flip() # update the display with all the .blit() changes 
