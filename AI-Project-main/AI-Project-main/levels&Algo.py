import numpy as np
import random
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

R_CNT = 6
C_CNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4


def creat_empty_board():
    board = np.zeros((R_CNT, C_CNT))
    return board


def put_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_loc(board, col):
    return board[R_CNT - 1][col] == 0


def get_open_row(board, col):
    for r in range(R_CNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(C_CNT - 3):
        for r in range(R_CNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(C_CNT):
        for r in range(R_CNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(C_CNT - 3):
        for r in range(R_CNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                    c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(C_CNT - 3):
        for r in range(3, R_CNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                    c + 3] == piece:
                return True


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, C_CNT // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(R_CNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(C_CNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score Vertical
    for c in range(C_CNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(R_CNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score posiive sloped diagonal
    for r in range(R_CNT - 3):
        for c in range(C_CNT - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(R_CNT - 3):
        for c in range(C_CNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


def minimax(board, depth, maximizingPlayer, difficulty):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_open_row(board, col)
            b_copy = board.copy()
            put_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth - 1, False, difficulty)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_open_row(board, col)
            b_copy = board.copy()
            put_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth - 1, True, difficulty)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value


def get_valid_locations(board):
    valid_locations = []
    for col in range(C_CNT):
        if is_valid_loc(board, col):
            valid_locations.append(col)
    return valid_locations


def alpha_beta(board, depth, alpha, beta, maximizingplayer, difficulty):
    valid_locations = get_valid_locations(board)
    terminal_node = is_terminal_node(board)
    if depth == 0 or terminal_node:
        if terminal_node:
            if winning_move(board, AI_PIECE):
                return (None, 1000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -100000)
            else:  # game is over
                return (None, 0)
        else:  # depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingplayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_open_row(board, col)
            b_copy = board.copy()
            put_piece(b_copy, row, col, AI_PIECE)
            new_score = alpha_beta(
                b_copy, depth - 1, alpha, beta, False, difficulty)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, column
    else:  # minimize player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_open_row(board, col)
            b_copy = board.copy()
            put_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = alpha_beta(
                b_copy, depth - 1, alpha, beta, True, difficulty)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, column


def GUI_board(board):
    for c in range(C_CNT):
        for r in range(R_CNT):
            pygame.draw.rect(screen, GREEN, (c * GUI_SIZE, r *
                             GUI_SIZE + GUI_SIZE, GUI_SIZE, GUI_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * GUI_SIZE + GUI_SIZE / 2), int(r * GUI_SIZE + GUI_SIZE + GUI_SIZE / 2)), radius)

    for c in range(C_CNT):
        for r in range(R_CNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (
                    int(c * GUI_SIZE + GUI_SIZE / 2), height - int(r * GUI_SIZE + GUI_SIZE / 2)), radius)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, BLUE, (
                    int(c * GUI_SIZE + GUI_SIZE / 2), height - int(r * GUI_SIZE + GUI_SIZE / 2)), radius)
    pygame.display.update()


board = creat_empty_board()
print_board(board)
game_end = False


# Ask the user to choose the algorithm
algorithm = input("Choose the algorithm (Minimax/Alpha_Beta): ")

# Ask the user to choose the difficulty level
difficulty_level = input("Choose the difficulty level (Easy/Medium/Hard): ")
# Use the appropriate AI function with the selected algorithm and depth


def choose_algo(algorithm=None, depth=None):
    if algorithm == "Minimax":
        col, score = minimax(board, depth, True, difficulty_level)
    else:
        col, score = alpha_beta(board, depth, -math.inf,
                                math.inf, True, difficulty_level)

# Set the corresponding depth value based on the difficulty level


def choose_level():
    if difficulty_level == "Easy":
        depth = 1
    elif difficulty_level == "Medium":
        depth = 3
    elif difficulty_level == "Hard":
        depth = 5


#
#
# # Set the difficulty level
# difficulty_level = "medium"  # "easy", "medium", or "hard"
#
# # Set the corresponding depth value based on the difficulty level
# if difficulty_level == "easy":
#     depth = 2
# elif difficulty_level == "medium":
#     depth = 4
# elif difficulty_level == "hard":
#     depth = 6
#
# # Use the appropriate AI function with the selected depth
# if difficulty_level == "easy":
#     col, score = minimax(board, depth, True)
# else:
#     col, score = alpha_beta(board, depth, -math.inf, math.inf, True,difficulty_level)
#


pygame.init()

GUI_SIZE = 100

width = C_CNT * GUI_SIZE
height = (R_CNT + 1) * GUI_SIZE

size = (width, height)

radius = int(GUI_SIZE / 2 - 5)

screen = pygame.display.set_mode(size)
GUI_board(board)
pygame.display.update()

font = pygame.font.SysFont("monospace", 30)

turn = 0

while not game_end:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, GUI_SIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(
                    screen, RED, (posx, int(GUI_SIZE / 2)), radius)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, GUI_SIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx / GUI_SIZE))

                if is_valid_loc(board, col):
                    row = get_open_row(board, col)
                    put_piece(board, row, col, PLAYER_PIECE)

                    if winning_move(board, PLAYER_PIECE):
                        titel = font.render(
                            " The RED player win, Congratulations! ", 1, GREEN)
                        screen.blit(titel, (20, 10))
                        game_end = True

                turn += 1

                print_board(board)
                GUI_board(board)

    # # Ask for Player 2 Input
    if turn == AI and not game_end:

        # col = random.randint(0, COLUMN_COUNT-1)
        # col = pick_best_move(board, AI_PIECE)
        col, minimax_score = minimax(board, 1,  True)

        if is_valid_loc(board, col):
            # pygame.time.wait(500)
            row = get_open_row(board, col)
            put_piece(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                titel = font.render(
                    " The Blue player win, Congratulations! ", 1, GREEN)
                screen.blit(titel, (20, 10))
                game_end = True

        print_board(board)
        GUI_board(board)

        turn -= 1

    while not game_end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Ask for Player 1 Input
        if turn == PLAYER:
            col, minimax_score = minimax(board, 5, True, difficulty_level)

            if is_valid_loc(board, col):
                row = get_open_row(board, col)
                put_piece(board, row, col, PLAYER_PIECE)

                if winning_move(board, PLAYER_PIECE):
                    titel = font.render(
                        "The RED player win, Congratulations!", 1, GREEN)
                    screen.blit(titel, (20, 10))
                    game_end = True

            print_board(board)
            GUI_board(board)

            turn += 1

        # Ask for Player 2 Input
        if turn == AI and not game_end:
            col, minimax_score = minimax(board, 5, True, difficulty_level)

            if is_valid_loc(board, col):
                row = get_open_row(board, col)
                put_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    titel = font.render(
                        "The Blue player win, Congratulations!", 1, GREEN)
                    screen.blit(titel, (20, 10))
                    game_end = True

            print_board(board)
            GUI_board(board)

            turn -= 1

        if game_end:
            pygame.time.wait(3000)
