from math import pi
r = float(input ("Input the radius of the circle : "))
print("")
print( "unformatted result", pi * r**2 )
print ("The area of the circle with radius " + str(r) + " is: " + str( round( pi * r**2, 3 ) ) )
print ("The area of the circle with radius " + str(r) + " is: " + str( format( pi * r**2, '.3f' ) ) )
print ("The area of the circle with radius " + str(r) + " is: ") 
print("{0:.3f}".format( round( pi * r**2,3 ) ))
print("")
#
value = 2.34558
precision = 2
width = 4
#
#print(f'result: {value:{width}.{precision}f}')   # python 3.6+
#eof
