# calculator program
#
def add(x,y):
	return int(x) + int(y)
def sub(x,y):
	return int(x) - int(y)
def mul(x,y):
	return int(x) * int(y) 
def div(x,y):
	return int(x) / int(y)
#
def menu():
    #print what options you have
    print ("Welcome to calculator.py")
    print ("your options are:")
    print (" ")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator.py")
    print (" ")
    return input ("Choose your option: ")
#
choice = ""
result = 0
while choice != "5":
	choice = menu()
	print(choice)
	if choice == "1":
		a = input()
		b = input()
		print("Add this: ", a, " to this: ", b)
		result = add(a,b)
	elif choice == "2":
		a = input()
		b = input()
		print("Subtract this: ", a, " from this: ", b)
		result = sub(a,b)
	elif choice == "3":
		a = input()
		b = input()
		print("Multiply this: ", a, " by this: ", b)
		result = mul(a,b)
	elif choice == "4":
		a = input()
		b = input()
		print("Divide this: ", a, " by this: ", b)
		result = div(a,b)
	if choice != "5":
		print("The result is ", result, "\n\n")
#
print("Program Ended")
# eof
