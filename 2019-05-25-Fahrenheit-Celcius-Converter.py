# Fahrenheit/Celcius Temperature Converter
fc = input("Please enter (F)ahrenheit or (C)elsius: ")
print("")
temp = int(input("Please enter temperature: "))
print("")
if fc.upper() == "C":
	new_temp = int(round((9 * temp) / 5 + 32))
	print( temp, "converted from Celsius to Fahrenheit is ", new_temp, "degrees" )
elif fc.upper() == "F":
	new_temp = int(round((temp - 32) * 5 / 9))
	print( temp, "converted from Fahrenheit to Celsius is ", new_temp, "celcius" )
#eof
