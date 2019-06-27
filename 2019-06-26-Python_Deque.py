# Python 3.7
# https://book.pythontips.com/en/latest/collections.html

from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'
d = deque(range(5))
print(len(d))
# Output: 5

d.popleft()
# Output: 0

d.pop()
# Output: 4

print(d)
# Output: deque([1, 2, 3])
d = deque([0, 1, 2, 3, 5], maxlen=5)
print(d)
# Output: deque([0, 1, 2, 3, 5], maxlen=5)

d.extend([6])
print(d)
#Output: deque([1, 2, 3, 5, 6], maxlen=5)
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
# Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
