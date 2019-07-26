# Python program that checks for prime numbers
# https://www.dotnetperls.com/prime-python
# Tested on https://repl.it/languages/Python3
# Python 3.7.8
def isprime(candidate):
    # No primes are even except 2.
    # ... Use modulo division to test for even numbers.
    if (candidate % 2) == 0:
        if candidate == 2:
            return True
        else:
            return False

    # Loop over numbers incrementing by 2 to the number.
    for i in range(3, candidate, 2):
        # No prime can be more than the square root.
        if (i * i) > candidate:
            break;
        # See if the number is evenly divisible.
        if (candidate % i) == 0:
            return False

    # The candidate is a prime unless it is 1.
    return candidate != 1

# Test for primes in first 100 numbers.
for test in range(0, 100):
    if isprime(test):
        print(test)

# Test for primes in another range.
for test in range(10000, 10100):
    if isprime(test):
        print(test)
