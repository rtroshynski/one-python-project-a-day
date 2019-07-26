# Python program that uses recursion
# https://www.dotnetperls.com/recursion-python
# Tested on https://repl.it/languages/Python3
# Python 3.7.8
def change(coins, amounts, highest, sum, goal):
    # See if we are done.
    if sum == goal:
        display(coins, amounts)
        return

    if sum > goal:
        return

    for value in amounts:
        if value >= highest:
            # Copy the coins list, then add the current value.
            copy = coins[:]
            copy.append(value)
            # Recursively add more coins.
            change(copy, amounts, value, sum + value, goal)

def display(coins, amounts):
    # Display our coins sorted by amount.
    for amount in amounts:
        count = coins.count(amount)
        print(amount, ":", count)
    print("")

coins = []
amounts = [1, 5, 10, 25, 50]
# Begin.
change(coins, amounts, 0, 0, 51)
# eof
