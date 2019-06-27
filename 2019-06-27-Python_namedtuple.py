# Python 3.7
# https://book.pythontips.com/en/latest/collections.html
from collections import namedtuple

# You can think of namedtuples like dictionaries but 
# unlike dictionaries they are immutable
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'

# attributes in namedtuples are immutable
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
# perry.age = 42  # error - cannot change attribute 

# Output: Traceback (most recent call last):
#            File "", line 1, in
#         AttributeError: can't set attribute

# use named tuples to make your code self-documenting. 
# They are backwards compatible with normal tuples. 
# It means that you can use integer indexes with 
# namedtuples as well
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
# Output: perry

# convert a named tuple to a dictionary 
Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
# Output: OrderedDict([('name', 'Perry'), ('age', 31), ...
# eof
