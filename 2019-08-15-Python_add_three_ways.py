# Python 3.7.4
# based on https://www.techiedelight.com/add-two-numbers-without-using-addition-operator/
# Tested on https://repl.it 

def add1(a,b):
  return a-(-b)

def add2(a,b):
  while(a > 0):
    b += 1
    a -= 1
  while(a < 0):
    b -= 1
    a += 1
  return b

def add3(a,b):
  if (not(b)):
    return a
  sum = a ^ b  
  carry = ( a & b) << 1
  return( add1(sum,carry))
def add4(a,b):
  return log(exp(a) * exp(b))

print(add1(3,2))
print(add2(3,2)) 
print(add3(3,2)) 
# eof 
