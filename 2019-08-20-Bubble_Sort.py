# Python 3.7.4
# https://github.com/OpenGenus/cosmos/blob/master/code/sorting/src/bubble_sort/bubble_sort.py
# Tested on https://repl.it 

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr = [4,2,8,9,4,5,0]
print(bubble_sort(arr)) 
# eof
