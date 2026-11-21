#Kubra Cakici Lab 03
#Topics: modern primality and factorization.
#1. Miller-Rabin algorithm. It will work for numbers of arbitrary size
import random
import math
import time

#for the test i will do for n(odd, n>3) and k(number of iterations)
def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod
    return result

#this function returns True if n is composite, False if n is probably prime
def witness(a, n, s, d):
    #if it turns true, then n is composite
    x = mod_pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True


def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

#base cases for small numbers
    if n< 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    #we write  n-1 as 2^s * d
    s = 0
    d = n - 1

    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        if witness(a, n, s, d):
            return False
    return True


#testing the miller_rabin function
#for testing we use a list of prime and composite numbers, including some large primes and composites. We will also measure the time taken for each test.
if __name__ == "__main__":
    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                    101, 103, 107, 109, 113,
                    #composite numbers
                    4,6,8,9,10,
                    #large primes
                    15485863,
                    #large composite
                    15485863*15485867,
                    #arbitrary large prime
                    32416190071,2**61 - 1, 2**521 - 1,
                    #arbitrary large composite
                    32416190071 * 32416190073, (2**89 - 1) * (2**107 - 1)]

    k = 5
    #k is the number of iterations for the miller -rabin test
    #the reason for choosing k=5 is that it provides a good balance between accuracy and performance.
    #increasing k increases the accuracy of the test, but also increases the time taken for each test. 
    for num in test_numbers:
        start_time = time.time()
        result = miller_rabin(num, k)
        end_time = time.time()
        print(f"Number: {num}, Is Prime: {result}, Time Taken: {end_time - start_time:.6f} seconds")


    
    
