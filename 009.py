"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# Finding pythagorean triplet using Dickinson Method
def pythagorean_triplet():
    for r in range(1,1000):
        for s in range(1,r):
            if ((r**2)/2)%s == 0:
                t = ((r**2)/2)/s
                if (r+ s + r + t + r + s + t) == 1000:
                    return (r+s) * (r+t) * (r + s + t)


print(pythagorean_triplet())