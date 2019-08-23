# Python 3.7.4
# https://pynative.com/python-data-structure-exercise-for-beginners/
# Tested on https://repl.it  

# given two lists, pick the odd element from both
# and merge the lists 
# start the first list at 1 Index
# start the second list at 0 index 

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()
oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)
EvenElement = listTwo[0::2]
print("Element at odd-index positions from list two")
print(EvenElement)
print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)
# eof
