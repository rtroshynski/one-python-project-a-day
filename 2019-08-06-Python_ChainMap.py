# Python 3.7.4
# https://pymotw.com/3/collections/chainmap.html
# Tested on https://repl.it

import collections

# Accessing Values

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))

#-----------------------------------------------

# Reordering - When the list of mappings is reversed, 
# the value associated with 'c' changes

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))

#-----------------------------------------------

# Updating Values

# A ChainMap does not cache the values in the child mappings.
# Thus, if their contents are modified, the results are 
# reflected when the ChainMap is accessed

# Changing the values associated with existing keys and 
# adding new elements works the same way.

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))

# It is also possible to set values through the ChainMap 
# directly, although only the first mapping in the chain 
# is actually modified.

# When the new value is stored using m, the a mapping is updated.

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before:', m)
m['c'] = 'E'
print('After :', m)
print('a:', a)

#-----------------------------------------------

# ChainMap provides a convenience method for 
# creating a new instance with one extra mapping 
# at the front of the maps list to make it easy 
# to avoid modifying the existing underlying data structures.

# This stacking behavior is what makes it convenient to 
# use ChainMap instances as template or application contexts. 
# Specifically, it is easy to add or update values in one 
# iteration, then discard the changes for the next iteration.

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 before:', m1)
print('m2 before:', m2)

m2['c'] = 'E'

print('m1 after:', m1)
print('m2 after:', m2)

#-----------------------------------------------

# For situations where the new context is known or built in 
# advance, it is also possible to pass a mapping to new_child().

# This is the equivalent of
#
# 		m2 = collections.ChainMap(c, *m1.maps)

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c

# eof
