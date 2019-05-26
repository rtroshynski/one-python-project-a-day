# Fahrenheit/Celcius Temperature Converter
fc = input("Please enter (F)ahrenheit or (C)elsius: ")
print("")
temp = int(input("Please enter temperature: "))
print("")
if fc == "C":
	new_temp = 9.0/5.0 * temp + 32
	print( temp, "converted from Celsius to Fahrenheit is ", new_temp )
elif fc == "F":
	new_temp = (temp - 32) * 5.0/9.0
	print( temp, "converted from Fahrenheit to Celsius is ", new_temp )
#eof
