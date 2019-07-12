# Python 3.6.8
# this is the start of developing a program that can play
# the board game battleship.  This isn't a complete program
# but one of many steps to take before it is done.

import random
import collections

#types of ships
ships = {"Aircraft Carrier":5,
		 "Battleship":4,
 		 "Submarine":3,
		 "Destroyer":3,
		 "Patrol Boat":2
		 }

def print_ships(ships):
	for k, v in collections.OrderedDict(sorted(ships.items())).items():
		print(k, v)

board1 = []
board2 = [] 

def init_board(board):
  #initializing board
  for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print (" ".join(row))

def random_horizontal_vertical():
  return random.randint(0,1)

#defining where the ship is
def random_row(board):
    return random.randint(1, len(board) - 1)

def random_col(board):
    return random.randint(1, len(board) - 1)

def play_game():
  pass

def configure_board(board):
  for ship,length in ships.items():
    #print(ship,":",length)
    rr_row = random_row(board)
    rr_col = random_col(board)
    h_or_v = random_horizontal_vertical()
    board_length = len(board) 
    #
    if h_or_v == 1: # horizontal 
      if rr_row + length <= board_length:
        for i in range(rr_row,length):
          board[i][rr_col] = '*'
    else: # vertical 
      if rr_col + length <= board_length:
        for i in range(rr_col,length): 
          board[rr_row][i] = '*'

  print("\n") 

def main():
  print_ships(ships) 
  print("\n")
  print("Player 1\n")
  init_board(board1) 
  configure_board(board1) 
  print_board(board1) 
  print("\n") 
  print("Player 2\n")
  init_board(board2) 
  configure_board(board2)
  print_board(board2) 
  print("\n") 

if __name__ == '__main__':
  print("Let's play Battleship!\n")
  main() 
#eof 
