# Python 3.7
# https://codescracker.com/python/program/python-program-find-factors-of-number.htm
count = 0
number = 100
for i in range(2, number-1):
	if number%i == 0:
		print(i)
		i += 1;
		count += 1
if count==0:
	print(number,"is a prime number.")
#eof
