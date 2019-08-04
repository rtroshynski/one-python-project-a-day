# Python 3.7.4
# https://www.dotnetperls.com/sort-python
# Tested at https://repl.it/languages/Python3

# Contains unsorted, positive and negative integers.
elements = [100, 200, 0, -100]

# Sort from low to high.
elements.sort()
print(elements)

# using reversed, sorted

elements = [22, 333, 0, -22, 1000]

# Use a reversed, sorted view: a descending view.
view = reversed(sorted(elements))

# Display our results.
for element in view:
    print(element)

# using sorted, key, reverse

# An array of color names.
colors = ["blue", "lavender", "red", "yellow"]

# Sort colors by length, in reverse (descending) order.
for color in sorted(colors, key=lambda color: len(color), reverse=True):
    print(color)

# sorting on dictionary keys

# A dictionary with three pairs.
furniture = {"table": 1, "chair": 2, "desk": 4}

# Get sorted view of the keys.
s = sorted(furniture.keys())

# Display the sorted keys.
for key in s:
    print(key, furniture[key])

# sorting list of objects

class Bird:
    def __init__(self, weight):
        self.__weight = weight

    def weight(self):
        return self.__weight

    def __repr__(self):
        return "Bird, weight = " + str(self.__weight)

# Create a list of Bird objects.
birds = []
birds.append(Bird(10))
birds.append(Bird(5))
birds.append(Bird(200))

# Sort the birds by their weights.
birds.sort(key=(lambda b: b.weight()))

# Display sorted birds.
for b in birds:
    print(b)

# benchmarks sorted, reversed

import time

data = ["carrot", "apple", "peach", "nectarine"]

print(time.time())

# Version 1: use sort and reverse.
i = 0
while i < 1000000:
    v = 0
    data.sort()
    for element in data:
        v += 1
    data.reverse()
    for element in data:
        v += 1
    i += 1

print(time.time())

# Version 2: use sorted and reversed.
i = 0
while i < 1000000:
    v = 0
    for element in sorted(data):
        v += 1
    for element in reversed(data):
        v += 1
    i += 1

print(time.time())

# sorting string chars

value = "boat"

# Get list comprehension of characters and sort the list.
list = [c for c in value]
list.sort()

# Join the characters together.
result = "".join(list)
print(result)
