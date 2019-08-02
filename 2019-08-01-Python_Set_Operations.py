# Python Set Operations
# Python 3.7.4
# https://medium.com/towards-artificial-intelligence/50-python-3-tips-tricks-e5dbe05212d7
# Tested on https://repl.it/languages/Python3
A = {1, 2, 3, 3}
print(A) 
B = {3, 4, 5, 6, 7}
print(B)  
print(A | B)  
print(A & B)  
print(A - B) 
print(B - A) 
print(A ^ B) 
print((A ^ B) == ((A - B) | (B - A)))
# eof
