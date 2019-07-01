# Python 3.7
# program to determine if a given number is a power of 2
# https://stackoverflow.com/questions/19383248/find-if-a-number-is-a-power-of-two-without-math-function-or-log-function
def power_of_two(i):
	return (i & (i - 1)) == 0
print(power_of_two(2))
print(power_of_two(3))
#eof
