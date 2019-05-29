# https://www.programiz.com/python-programming/examples/quadratic-roots
import cmath
# solving quadratic equation
print("This will solve a quadratic equation such that ax^2 + bx + c = 0")
a = 1
b = 5
c = 6
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
#
print('The solution are {0} and {1}'.format(sol1,sol2))
#eof
