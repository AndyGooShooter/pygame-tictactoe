### IMPORTS (libraries and functions from other files)
import pygame
import settings


### UPDATE DISPLAY
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

player = turn % 2 # 0 is white, 1 is black
            
board[click_col][click_row] = player # making the move in the array

# getting coordinates for the point
def rendering_points(row, col):
    build_x = settings.master_offset + (row - 1) * settings.master_square_w 
    build_y = settings.master_offset + (col - 1) * settings.master_square_h
    return (build_x, build_y)
build_x = settings.master_offset + (click_row - 1) * settings.master_square_w 
build_y = settings.master_offset + (click_col - 1) * settings.master_square_h

if player == 0: # making the move on the display
    screen.blit(white_point, (build_x, build_y))
else:
    screen.blit(black_point, (build_x, build_y))

turn += 1