# Python 3.6.8
# this is the start of developing a program that can play
# the board game battleship.  This isn't a complete program
# but one of many steps to take before it is done.

import random
#types of ships
ships = {"Aircraft Carrier":5,
		 "Battleship":4,
 		 "Submarine":3,
		 "Destroyer":3,
		 "Patrol Boat":2
		 }

#print(ships.keys())
#print(ships.values())
#print(ships.items())
#for k,v in ships.items():
#    print(k, v)

# sorted
import collections
for k, v in collections.OrderedDict(sorted(ships.items())).items():
    print(k, v)

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

"""
In initializing the board, the ship_row and ship_col
numbers represent a starting point on the board.  the
next step is to determine the orientation of the ships
as well as which ship to put there and whether or not
the ship overlaps another ship.

So, generate a random x,y and h/l then figure out if then
given ship can fit in the space.  If not, generate another
random x,y. 
"""
def random_horizontal_vertical():
  return random.randint(0,1)

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
