# Program to find the factorial of an integer
x = int(input("Enter a number: "))
print(x)

if x > 0:
	fact = 1
	for i in range(1, x + 1):
		fact = fact * i
	print( x ,"factorial is ", fact)
elif x == 0:
	print("The factorial of 0 is 1")
elif x < 0:
	print("Sorry, factorial does not exist for negative numbers")
#eof
