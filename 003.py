"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math

def main():
    # Empty list stores prime factors of number
    prime_factor = []

    # Number question prompts us for
    n = 600851475143

    # Check up to floor of |_n_| take integer square root 
    for i in range(2, int(math.sqrt(n))):

        # Determines if i is a factor of n
        if n % i == 0:
            # Call function to check if factor is prime
            if check_prime(i):

                # Adds prime factor to prime_factor list
                prime_factor.append(i
                                    )
            # for each factor i b/w 2 and int(sqrt(n)) n/i also a factor
            if check_prime(n/i):

                # Add prime factor to prime_factor list
                prime_factor.append(i)
    
    # Print the max prime factor from list
    print(max(prime_factor))
                    
# Function checks if factor is prime or not
def check_prime(x):
    for b in range(2, int(math.sqrt(x))):
        if x % b == 0:
            return False      
    return True


if __name__ == '__main__':
    main()
