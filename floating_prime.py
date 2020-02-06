# The Internship - 2
# Gorramuth Prasertkull
# Program to check if input is floating prime

import math

def isPrime(num):

    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # If any of the divisors up to the square of the number
    # have no remainder, then it is not a prime
    squareOfNum = int(math.sqrt(num))
    for divisor in range(3, 1 + squareOfNum, 2):
        if num % divisor == 0:
            return False
    return True

def isFloatingPrime(num):

    for times in range(3):
        num = num * 10
        if isPrime(int(num)):
            return True
            break

    return False

while(True):

    num = float(input())
    if num == 0.0:
        break
    output = "TRUE" if isFloatingPrime(num) else "FALSE"
    print(output)


