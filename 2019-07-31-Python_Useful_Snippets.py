# Useful Python Snippets
# Python 3.7.4
# http://fadymak.com/pages/useful_python_snippets.html
# Test on https://repl.it/languages/Python3
"""
You want to group the data by the type of animal to return a list of dogs and a list of cats. Thankfully, Python's itertools has a groupby function that allows you to do this easily:
"""

from itertools import groupby
import pprint as pp

data = [
    {'animal': 'dog', 'name': 'Roxie', 'age': 5},
    {'animal': 'dog', 'name': 'Zeus', 'age': 6},
    {'animal': 'dog', 'name': 'Spike', 'age': 9},
    {'animal': 'dog', 'name': 'Scooby', 'age': 7},
    {'animal': 'cat', 'name': 'Fluffy', 'age': 3},
    {'animal': 'cat', 'name': 'Oreo', 'age': 5},
    {'animal': 'cat', 'name': 'Bella', 'age': 4}   
    ]

grouped_data = {}

for key, group in groupby(data, lambda x: x['animal']):
    grouped_data[key] = [thing['name'] for thing in group]

pp.pprint(grouped_data)
# eof
