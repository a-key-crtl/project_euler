"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
from math import gcd

a = 20
final = 1

# LCM accumulation where LCM of A * B is defined as A*B / gcd(A,B)
for i in range(2, a+1):
    final = final* i//gcd(final,i)
print(final)

