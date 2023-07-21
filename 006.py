"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

# Compute square of the usm of first ten natural numbers
def square_of_sum(x):
    sum_total = 0
    while x < 101:
        sum_total = sum_total + x
        x = x + 1
    return pow(sum_total, 2)

# Compute sum of the squares of the first ten natural numbers
def sum_of_squares(y):
    square_total = 0
    while y < 101:
        square_total = square_total + pow(y, 2)
        y = y + 1    
    return square_total

# Subtract sum of squares from square of sum 
difference = -(2640 + sum_of_squares(11)) + (385 + square_of_sum(11))

# Print difference
print(difference)