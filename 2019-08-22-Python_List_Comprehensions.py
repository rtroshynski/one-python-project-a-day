# Python 3.7.4
# https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
# Tested on https://repl.it/languages/Python3

# list comprehension
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [n * 2 for n in numbers]  # no if 
print(doubled_numbers)
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
print(doubled_odds)
# eof
