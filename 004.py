"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Verify product is a palindrome
def is_pal(c):
    return int(str(c)[::-1]) == c

# Initial palindrome value is 0 updates each for loop iteration
max_palindrome = 0

# Counts down from 999
for a in range(999, 99, -1):
    # counts from 100
    for b in range(99, 999, 1):
        # multiplies loop of 999 descending and 99 ascending
        prod = a * b
        # is product is a palindrome and greater than max palindrome value update
        if is_pal(prod) and prod > max_palindrome:
            max_palindrome = prod

# print largest palindrome made from product of two 3-digit numbers
print(max_palindrome)
