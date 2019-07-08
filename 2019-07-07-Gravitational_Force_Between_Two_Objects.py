# Python 3.7
m1=float(1000000)    # mass of first object 
m2=float(500000)     # mass of second object
r=float(20)          # distance between both objects
G=6.673*(10**-11)    # gravitational constant
f=(G*m1*m2)/(r**2)
print("The gravitational force is: ",round(f,2),"N")
# eof
