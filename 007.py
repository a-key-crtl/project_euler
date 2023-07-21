"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

def isPrime(n):
    if n < 2:
        return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nPrime(n):
    numb_of_primes = 0
    prime = 1
    
    while numb_of_primes < n:
        prime += 1
        if isPrime(prime):
            numb_of_primes += 1
    return prime

print(nPrime(10001))