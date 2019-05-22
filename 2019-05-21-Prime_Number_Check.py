# Check if the input number is prime or not
x = int(input("Enter a candidate prime: "))
print(x)

# prime numbers are greater than 1
if x > 1:
   # check for factors
   for i in range(2,int(x**0.5)):
       if (x % i) == 0:
           print(x,"is not a prime number")
           print(i,"times",x//i,"is",x)
           break
   else:
       print(x,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(x,"is not a prime number")
#eof
