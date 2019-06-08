# https://realpython.com/how-to-implement-python-stack/
# simple stack implementation using lists
myStack = []
myStack.append('a')
myStack.append('b')
myStack.append('c')
print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
#
from collections import deque
myStack = deque()
myStack.append('a')
myStack.append('b')
myStack.append('c')
print(myStack)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
#
# thread-safe
from queue import LifoQueue
myStack = LifoQueue()
myStack.put('a')
myStack.put('b')
myStack.put('c')
print(myStack)
print(myStack.get())
print(myStack.get())
print(myStack.get())
#eof
