# Python 3.7.4
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# Tested on htts://repl.it 

# Python code to demonstrate working of 
# heapify(), heappush() and heappop() 

# importing "heapq" to implement heap queue 
import heapq 

# initializing list 
li = [5, 7, 9, 1, 3] 

# using heapify to convert list into heap 
heapq.heapify(li) 

# printing created heap 
print ("The created heap is : ",end="") 
print (list(li)) 

# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(li,4) 

# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(li)) 

# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(li)) 
# Python code to demonstrate working of 
# heappushpop() and heapreplce() 

# initializing list 1 
li1 = [5, 7, 9, 4, 3] 

# initializing list 2 
li2 = [5, 7, 9, 4, 3] 

# using heapify() to convert list into heap 
heapq.heapify(li1) 
heapq.heapify(li2) 

# using heappushpop() to push and pop items simultaneously 
# pops 2 
print ("The popped item using heappushpop() is : ",end="") 
print (heapq.heappushpop(li1, 2)) 

# using heapreplace() to push and pop items simultaneously 
# pops 3 
print ("The popped item using heapreplace() is : ",end="") 
print (heapq.heapreplace(li2, 2)) 

# Python code to demonstrate working of 
# nlargest() and nsmallest() 

# initializing list 
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1] 

# using heapify() to convert list into heap 
heapq.heapify(li1) 

# using nlargest to print 3 largest numbers 
# prints 10, 9 and 8 
print("The 3 largest numbers in list are : ",end="") 
print(heapq.nlargest(3, li1)) 

# using nsmallest to print 3 smallest numbers 
# prints 1, 3 and 4 
print("The 3 smallest numbers in list are : ",end="") 
print(heapq.nsmallest(3, li1)) 

# eof 
