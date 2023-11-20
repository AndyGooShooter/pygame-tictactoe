### IMPORTS (libraries and functions from other files)
import pygame
import settings



### BOARD ARRAY
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
def legal_move(row, col):
    if row > 8 or row < 1 or col > 8 or col < 1: # if the square is already occupied
        return False
    if(board[row][col] != 0): # if the square is already occupied
        return False
    return True

def make_move(row, col, player):
    
    board[row][col] = player
    return 0

def render(screen, white_point, black_point):
    for i in range(1, 9):
        for j in range(1, 9):
            build_x = settings.master_center_offset + settings.master_offset + (i - 1) * settings.master_square_w
            build_y = settings.master_center_offset + settings.master_offset + (j - 1) * settings.master_square_h
            if board[i][j] == 1:
                screen.blit(white_point, (build_x, build_y))
            elif board[i][j] == 2:
                screen.blit(black_point, (build_x, build_y))
