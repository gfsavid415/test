# primes.py
from math import sqrt, ceil

def get_primes(n):
    """Calculate a list of primes up to n (included). """
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))  # division limit
        for prime in primelist:  # we try only the primes
            if prime > root:  # no need to check any further
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist
	
n = 100
print(get_primes(n))

""" Gemma's prime version
from math import sqrt, ceil

def get_primes(n):
    prime_list = []
    for candidate in range(2, n+1):
        root  = ceil(sqrt(candidate))
        for prime in prime_list:
            if prime <= root:
                if candidate % prime == 0:
                    break
        else:
            prime_list.append(candidate)

    return prime_list

n = 100
print(get_primes(n))
"""