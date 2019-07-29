# Python conversions  
# https://www.dotnetperls.com/convert-python
# Tested on https://repl.it/languages/Python3
# Python 3.7.4

vegetables = ("carrot", "squash", "onion")

# Convert to list.
veg2 = list(vegetables)
veg2.append("lettuce")

# Print results.
print(vegetables)
print(veg2)
#
# Convert tuple and string 
tup = ("rabbit", "mouse", "gorilla", "giraffe")

# Join tuple with no space.
s = "".join(tup)
print(s)

# Join tuple with slash.
s = "/".join(tup)
print(s)
#
# Convert list and string 
vehicles = ["car", "truck", "tractor"]

# Convert list to string with join.
result = "".join(vehicles)

# Convert with semicolons separating strings.
result2 = ";".join(vehicles)

print(result)
print(result2)
#
# Convert dictionary 
vegetables = {"carrot": 1, "squash": 2, "onion": 4}

# Convert dictionary to list of tuples.
items = list(vegetables.items())

for item in items:
    print(len(item), item)
# 
# Converts to int  
floating = 1.23456

# Convert to int and print.
print(floating)
print(int(floating))
# 
# convert number to string  
# Convert number to string.
number = 123
value = str(number)

# Print the string and its character count.
print(value)
print(len(value))

# Convert string to number.
number2 = int(value)

# Print the number and add one.
print(number2)
print(number2 + 1)
#
# Convert class to string  
class Test:
    def __init__(self):
        self.size = 1
        self.name = "Python"

    def __repr__(self):
        # Return a string.
        return "Size = " + str(self.size) + ", Name = " + str(self.name)

t = Test()

# Str and repr will both call into __repr__.
s = str(t)
r = repr(t)

# Display results.
print(s)
print(r)
#
# gets list of chars 
value = "cat"

# Get chars from string with list comprehension.
list = [c for c in value]

print(list)
#
# Converts bytes, string  
# Convert from string to bytes.
value = "carrot"
data = bytes(value, "ascii")
print(data)

# Convert bytes into string with decode.
original = data.decode("ascii")
print(original)
#
# converts bytes, megabytes  
def bytestomegabytes(bytes):
    return (bytes / 1024) / 1024

def kilobytestomegabytes(kilobytes):
    return kilobytes / 1024

# Convert 100000 bytes to megabytes.
megabytes1 = bytestomegabytes(100000)
print(100000, "bytes =", megabytes1, "megabytes")

# 1024 kilobytes to megabytes.
megabytes2 = kilobytestomegabytes(1024)
print(1024, "kilobytes =", megabytes2, "megabytes")
#eof  
