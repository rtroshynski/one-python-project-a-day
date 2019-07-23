# Python 3.6.8
# https://www.dotnetperls.com/class-python
# Python program that uses class
class Box:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height

# Create an instance of Box.
x = Box(10, 2)

# Print area.
print(x.area())
#
# Python program that uses class inheritance 
class A:
    def width(self):
        print("a, width called")

class B(A):
    def size(self):
        print("b, size called")

# Create new class instance.
b = B()
# Call method on B.
b.size()
# Call method from base class.
b.width()
#
# Python program that uses two underscore varialble
class A:
    # Init.
    def __init__(self, value):
        self.__value = value

    # Two-underscore name.
    __value = 0

# Create the class.
a = A(5)

# [1] Cannot use two-underscore name.
# print(a.__value)

# [2] Must use mangled name.
print(a._A__value)
#
# Python program that uses subclass
class A:
    def hello(self):
        print("A says hello")

class B(A):
    def hello(self):
        print("B says hello")

# Use the derived class.
b = B()
b.hello()

# See if B inherits from A.
if issubclass(B, A):
    print(1)

# See if A inherits from B.
if issubclass(A, B):
    # Not reached.
    print(2)

# See if A inherits from itself.
if issubclass(A, A):
    print(3)
#
# Python program that uses isinstance
class A:
    def welcome(self):
        # Not called.
        print("Welcome")

# This is an instance of A.
a = A()

if isinstance(a, A):
    print(1)

# This is an instance of the list class.
b = [1, 2, 3]

if isinstance(b, A):
    # Not reached.
    print(2)

if isinstance(b, list):
    print(3)
#
# Python program that uses repr
class Snake:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return "Snake, type = " + self.type

# Create Snake instance.
# ... Print its repr.
s = Snake("Anaconda")
print(s)

# Get repr of Snake.
value = repr(s)
print(value)
#
# Python program that uses property
class Snake:
    def getname(self):
        return self._name

    def setname(self, value):
        # When property is set, capitalize it.
        self._name = value.capitalize()

    name = property(getname, setname)

# Create a snake instance.
s = Snake()

# Set name property.
s.name = "rattle"

# Get name property.
print(s.name)
#
# Python program that uses super 
class Shape:
    def name(self):
        print("Shape")

class Circle(Shape):
    def name(self):
        print("Circle")
        # Call name method from parent class.
        super().name()

# Create Circle and call name.
c = Circle()
c.name()
#
# Python program that uses hash on class
class Snake:
    def __init__(self, name, color, unique_id):
        self.name = name
        self.color = color
        self.unique_id = unique_id
    def __hash__(self):
        # Hash on a unique value of the class.
        return int(self.unique_id)

# Hash now is equal to the unique ID values used.
p = Snake("Python", "green", 55)
print(hash(p))

p = Snake("Python", "green", 105)
print(hash(p))
#
# Python program that uses id
class Cat:
    def __init__(self, color):
        self.color = color

cat1 = Cat("black")
cat2 = Cat("orange")

# Each object has a unique id.
# ... The ids may vary between runs.
print(id(cat1))
print(id(cat2))
# eof 
