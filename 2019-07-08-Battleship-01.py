# Python 3.7
# this is the start of developing a program that can play
# the board game battleship.  This isn't a complete program
# but one of many steps to take before it is done.

import random
#initializing board
board = []
for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print (" ".join(row))

#starting the game and printing the board
print ("Let's play Battleship!")
#print_board(board)

#defining where the ship is
def random_row(board):
    return random.randint(1, len(board) - 1)

def random_col(board):
    return random.randint(1, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print( ship_row )
print( ship_col )
board[ship_row-1][ship_col-1] = '*'

print_board(board)
# eof
