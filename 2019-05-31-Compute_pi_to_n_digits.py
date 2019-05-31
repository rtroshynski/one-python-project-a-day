# https://github.com/microice333/Python-projects/blob/master/n_digit_pi.py
# generate pi to nth digit
# Chudnovsky algorihtm to find pi to n-th digit
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
import decimal
import math
#
def compute_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi
#
n = int(input("Please type number between 0-1000: "))
print(n)
print("")
x = compute_pi(n)
print("Computed value pi: ", x )
print("System value of pi: ", math.pi )
#print("Difference is: ", math.pi - x)
#eof
