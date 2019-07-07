#  Python 3.7
# https://www.sanfoundry.com/python-program-find-lcm-two-numbers/
a=5
b=3
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1
# eof
