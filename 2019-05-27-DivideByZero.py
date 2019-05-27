#dividebyzero
while true:
	# attempt to convert and divide values
	try:
		number1 = int(input('Enter numerator: '))
		number2 = int(input('Enter denominator:'))
		result = number1 / number2
	except ValueError: # tried to convert non-numeric value to int
		print('You must enter two integers\n')
	except ZeroDivisionError: #denominator was zero
		print('Attempted to divide by zero\n')
	else:  # executed only if no exceptions occur
		print(f'{number1:.3f} / {number2:.3f} = {result:/3f}')
		break
#eof - "Deitel: Python for Programmers"
