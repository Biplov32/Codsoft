import sys
import pygame
import numpy as np

pygame.init()

# colors
White = (255, 255, 255)
Brown = (128, 64, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Black = (0, 0, 0)

# Proportion and sizes
Width = 300
Height = 300
Line_width = 5
Board_rows = 3
Board_columns = 3
Square_size = Width // Board_columns
circle_r = Square_size // 3
circle_w = 15
cross_w = 25

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Unbeatable Tic Tac Toe AI')
screen.fill(Black)

board = np.zeros((Board_rows, Board_columns))

def draw_lines(color=White):
    for i in range(1, Board_rows):
        pygame.draw.line(screen, color, (0, Square_size * i), (Width, Square_size * i), Line_width)
        pygame.draw.line(screen, color, (Square_size * i, 0), (Square_size * i, Height), Line_width)

def draw_figures(color=White):
    for row in range(Board_rows):
        for col in range(Board_columns):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * Square_size + Square_size // 2), int(row * Square_size + Square_size // 2)), circle_r, circle_w)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * Square_size + Square_size // 4, row * Square_size + Square_size // 4), (col * Square_size + 3 * Square_size // 4, row * Square_size + 3 * Square_size // 4), cross_w)
                pygame.draw.line(screen, color, (col * Square_size + Square_size // 4, row * Square_size + 3 * Square_size // 4), (col * Square_size + 3 * Square_size // 4, row * Square_size + Square_size // 4), cross_w)

def mark_square(row, col, player):
    board[row][col] = player

def available_squares(row, col):
    return board[row][col] == 0

def is_board_full(check_board=board):
    for row in range(Board_rows):
        for col in range(Board_columns):
            if check_board[row][col] == 0:
                return False
    return True

def check_win(player, check_board=board):
    for col in range(Board_columns):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
    for row in range(Board_rows):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True

    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True

    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True

    return False

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board):
        return float('inf')
    elif check_win(1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(Board_rows):
            for col in range(Board_columns):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(Board_rows):
            for col in range(Board_columns):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(Board_rows):
        for col in range(Board_columns):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)

    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False

def restart_game():
    screen.fill(Black)
    draw_lines()
    for row in range(Board_rows):
        for col in range(Board_columns):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // Square_size
            mouseY = event.pos[1] // Square_size

            if available_squares(mouseY, mouseX):
                mark_square(mouseY, mouseX, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if best_move():
                        if check_win(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over:
                    if is_board_full():
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                player = 1
                game_over = False

    if not game_over:
        draw_figures()
    else:
        if check_win(1):
            draw_figures(Green)
            draw_lines(Green)
        elif check_win(2):
            draw_figures(Red)
            draw_lines(Red)
        else:
            draw_figures(Brown)
            draw_lines(Brown)

    pygame.display.update()
