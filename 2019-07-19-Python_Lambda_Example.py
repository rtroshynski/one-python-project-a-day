# Python 3.8
# https://www.engineeringbigdata.com/python-lambda-python-programming/
# ordinary function declaration and use
def addition(x, y):
    print(x + y)
addition(20, 10)
#
# simple lambda function and use
lambda_addition = lambda x, y: x + y
print(lambda_addition(20, 10))
#
# advanced lambda function and use
def power_lambda(n):
  return lambda x : x * n
multiple_10 = power_lambda(10)
print(multiple_10(5))
# eof
