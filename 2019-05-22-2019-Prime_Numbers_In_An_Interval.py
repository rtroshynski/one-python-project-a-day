# Display all the prime numbers within an interval
lower = int(input("Enter lower value: "))
print(lower)

upper = int(input("Enter upper value: "))
print(upper)

print("Prime numbers between",lower,"and",upper,"are:")

for x in range(lower,upper + 1):
   # prime numbers are greater than 1
   if x > 1:
       for i in range(2,int(x**0.5)):
           if (x % i) == 0:
               break
       else:
           print(x)
#eof
