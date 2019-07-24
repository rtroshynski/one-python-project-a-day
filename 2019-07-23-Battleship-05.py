"""
Still a work in progress.  Some code cleanup in this version
but not a working playable version yet
"""
# Python 3.6.8
import random
import collections

ships = {
    "Aircraft Carrier":5,
    "Battleship":4,
    "Submarine":3,
    "Destroyer":3,
    "Patrol Boat":2
}

orientation = {
	"horizontal":0,
	"vertial":1,
	"diagonal":2
}

status = ('Hit','Miss','Sunk')

shipLocations = { 
	'Aircraft Carrier': [], 
	'Battleship':[],
	'Submarine':[],
	'Destroyer':[],
	'Patrol Boat':[]
}

shipStatus = {
  "Aircraft Carrier" : 0,
  "Battleship":0,
  "Submarine":0,
  "Destroyer":0,
  "Patrol Boat":0
}

def print_ships(ships):
	for k, v in collections.OrderedDict(sorted(ships.items())).items():
		print(k, v)

board1 = [] # 2D list 
board2 = [] # 2D list 

def init_board(board):
  for x in range(10):
    board.append(["O"] * 10) 

def print_board(board):
    for row in board:
        print (" ".join(row))

def get_random(low,high):
	return random.randint(low,high)

def check_overlap(startingPoint, hv, length):
	pass

def play_game():
  pass

def configure_board(board):
  board_rows    = 10
  board_columns = 10

  horizontal    = 0
  vertical      = 1
  diagonal      = 2 

  for ship,length in ships.items():
    print(ship,":",length)
    row = get_random(0, len(board) - 1)  
    col = get_random(0, len(board) - 1)  
    hv  = get_random(horizontal,vertical)
    print (row, col, hv)
    board[row][col] = '*'
    """
    if hv == horizontal:
      if (col + length) <= (board_columns - 1):
        for i in range(col,length):
          board[row][i] = '*' 
    elif hv == vertical:
      if (row + length) <= (board_rows - 1):
        for i in range(row,length):
          board[i][col] = '*' 
      elif (row - length) >= 0:
        for i in range(row,row-length,-1):
          board[i][col] = '*' 
    elif hv == diagonal: 
      pass
    """ 
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
