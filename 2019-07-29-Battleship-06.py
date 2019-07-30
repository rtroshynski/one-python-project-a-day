# Python 3.7.4
# Tested on https://repl.it/languages/Python3
"""
Some test code to figure out how to work with coordinates in Python
"""

shipLocations = { 
	'Aircraft Carrier': [], 
	'Battleship':[],
	'Submarine':[],
	'Destroyer':[],
	'Patrol Boat':[]
}
shipLocations['Aircraft Carrier'].append((1,2))
shipLocations['Aircraft Carrier'].append((2,3))
print(shipLocations['Aircraft Carrier'])
if (1,2) in shipLocations['Aircraft Carrier']:
	print('success')
if (5,6) not in shipLocations['Aircraft Carrier']:
	print('success')
del shipLocations['Aircraft Carrier'][:]
print(shipLocations['Aircraft Carrier'])
# eof
