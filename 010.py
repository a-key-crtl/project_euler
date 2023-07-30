"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def isPrime(n):
    if n < 2:
        return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nPrime(n):
    prime = 1
    sum = 0
    
    while prime < n:
        prime += 1
        if isPrime(prime):
            sum = sum + prime
    return sum

print(nPrime(2000000))