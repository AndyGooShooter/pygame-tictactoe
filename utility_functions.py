### IMPORTS (libraries and functions from other files)
import settings
import pygame

dx = [0, 0, 1, 1, 1]
dy = [-1, 1, -1, 0, 1]

def is_in_matrix(x:int, y:int):
    return (0 < x < 9 and 0 < y < 9)

def is_legal_move(board, row:int, col:int):
    if not is_in_matrix(row, col): # if the square is outside the matrix
        return False
    
    if(board[row][col] != 0): # if the square is already occupied
        return False
    return True

def make_move(board, row, col, player):
    board[row][col] = player

def render(screen, board, white_point, black_point):
    for i in range(1, 9):
        for j in range(1, 9):
            build_x = settings.master_center_offset + settings.master_offset + (i - 1) * settings.master_square_w
            build_y = settings.master_center_offset + settings.master_offset + (j - 1) * settings.master_square_h
            if board[i][j] == 1 or board[i][j] == 100:
                screen.blit(white_point, (build_x, build_y))
            elif board[i][j] == 2 or board[i][j] == 200:
                screen.blit(black_point, (build_x, build_y))

def draw_line(screen, board):
    x_first = None
    y_first = None
    x_last = None
    y_last = None

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 100 or board[i][j] == 200:
                if x_first is None:
                    x_first = i
                    y_first = j
                x_last = i
                y_last = j

    start_x = settings.master_offset + settings.master_offset + (x_first - 1) * settings.master_square_w
    start_y = settings.master_offset + settings.master_offset + (y_first - 1) * settings.master_square_h
    end_x = settings.master_offset + settings.master_offset + (x_last - 1) * settings.master_square_w
    end_y = settings.master_offset + settings.master_offset + (y_last - 1) * settings.master_square_h

    pygame.draw.line(screen, (255, 0, 0), (start_x, start_y), (end_x, end_y), 5)
            

def check_dir(x:int, y:int, direction:int, cnt:int, board:list[list[int]], vis:list[list[bool]]) -> bool:
    if cnt == 4:
        board[x][y] *= 100
        return True

    vis[x][y] = True

    new_x = x + dx[direction]
    new_y = y + dy[direction]

    if is_in_matrix(new_x, new_y) and not vis[new_x][new_y] and board[x][y] == board[new_x][new_y]:
        r = check_dir(new_x, new_y, direction, cnt + 1, board, vis)
        if r:
            board[x][y] *= 100
        
        return r
    
    return False


def check_win(board:list[list[int]]):
    vis = [[False for _ in range(9)] for _ in range(9)]
    
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j]:
                for d in range(5):
                    new_i = i + dx[d]
                    new_j = j + dy[d]
                    if (is_in_matrix(new_i, new_j) and not vis[new_i][new_j]
                        and board[new_i][new_j] == board[i][j]):
                        r = check_dir(i, j, d, 1, board, vis)

                        if r:
                            return board[i][j] // 100

    return -1

if __name__ == '__main__':
    b = [[0 for i in range(9)] for i in range(9)]

    b[1][1] = b[2][2] = b[3][3] = 1
    b[1][2] = b[1][3] = b[1][4] = 1

    print(check_win(b))