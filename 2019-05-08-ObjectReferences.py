a = 100   # points to object 100 
b = a     # both point to identical object
a = 200   # a points to object 200 and b points to object 100
b = "foo" # b points to object "foo" but nothing points to object 100 so it will be garbage collected
print(a,b) # should print 200 foo
#eof
