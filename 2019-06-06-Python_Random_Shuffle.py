# https://pynative.com/python-random-shuffle/
from random import shuffle
#
number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print ("Original list : ",  number_list)
#
shuffle(number_list) #shuffle method
print ("List after first shuffle  : ",  number_list)
#
shuffle(number_list)
print ("List after second shuffle : ",  number_list)
#
string_list = ["Paint It Black", "Gimme Shelter", "Sympathy for the Devil", "Satisfaction", "You Cant Always Get What You Want"]
print ("Original String list: ",  string_list)
#
random.shuffle(string_list) #shuffle method
print ("String List after the first shuffle  : ",  string_list)
#
shuffle(string_list)
print ("String List after the second shuffle : ",  string_list)
#eof
