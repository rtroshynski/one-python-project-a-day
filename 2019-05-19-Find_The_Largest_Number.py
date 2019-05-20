x = 300
y = -1
z = 999

if (x >= y) and (x >= z):
   largest = x
elif (y >= x) and (y >= z):
   largest = y
else:
   largest = z

print(largest, "is the largest number between ",x,",",y,"and",z)
#eof
