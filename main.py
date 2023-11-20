### IMPORTS (libraries and functions from other files)
import pygame



### DISPLAY SIZES
# the entire background image
bg_h = 1890 
bg_w = 2100
offset = 105 # offset for board

# each square
square_h = 210 
square_w = 210

# each point
point_h = 30 
point_w = 30

display_multiplier = 0.2 # edit this to change the overall size of the display

# final display size
master_h = bg_h * display_multiplier 
master_w = bg_w * display_multiplier
master_offset = offset * display_multiplier # offset from the top left corner of the screen
master_square_h = square_h * display_multiplier
master_square_w = square_w * display_multiplier

### GAME CONFIGURATION
pygame.init()
screen = pygame.display.set_mode((master_h, master_w))
turn = 0 # turn counter, starts with 0
         # even numbers are white, odd numbers are black
# assets
bg = pygame.image.load("Assets/bg.png")
white_point = pygame.image.load("Assets/white_point.png")
black_point = pygame.image.load("Assets/black_point.png")

bg = pygame.transform.scale(bg, (master_h, master_w))
white_point = pygame.transform.scale(white_point, (master_h, master_w))
black_point = pygame.transform.scale(black_point, (master_h, master_w))


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
            turn += 1
            
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update() # update the display with all the .blit() changes 
