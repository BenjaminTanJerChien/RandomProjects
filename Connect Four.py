import numpy as np

row = 7
column = 7

def create_board():
    board = np.zeros((row, column))
    return board


def drop():
    pass

def is_valid_location(board, col):
    return board[5][col] == 0 

def next_open_space(board, col):
    for i in range(rows):
        if board[r][col] == 0:
            return r

board = create_board()
print(board)

game_over = False
turn = 0

while not game_over:


    #player 1 input
    if turn == 0 or turn % 2 == 0:
        selection = int(input("Player 1 make your selction (0-6)"))

    #player 2 input
    else:
        selection = int(input("Player 2 make your selction (0-6)"))

    turn += 1
    turn
    
