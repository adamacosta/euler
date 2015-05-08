import numpy as np
from euler_utils.primes import is_prime, smallprimes
from math import ceil, sqrt

# Factors, divisors, and multiples

def divisors(n):
    """Input: An integer n.
       Output: The divisors of n."""
    result = [1]
    if n > 1:
        result.append(n)
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result

def sum_divisors(n):
    """Input: A natural number n.
    Output: Sum of the divisors of n"""
    return sum(divisors(n))

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return abs((a // gcd(a, b)) * b)

def pollard_brent(n):
    """Input: An integer n.
       Output: The divisors of n."""
    if not n % 2: return 2
    if not n % 3: return 3

    y, c, m = np.random.randint(1, n), np.random.randint(1, n), np.random.randint(1, n)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g==1:
            ys = y
            for i in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x - y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1: break
    return g

def factors(n, sort=False):
    """Input: An integer n.
       Output: The prime factors of n."""
    if n == 0: return []
    if n < 0: n = abs(n)
    if is_prime(n): return [n]
    result = []
    for p in smallprimes:
        while not n % p:
            result.append(p)
            n //= p
        if p > n: break
    if n < 2: return result
    while n > 1:
        if is_prime(n):
            result.append(n)
            break
        # trial division did not fully factor, switch to pollard-brent
        factor = pollard_brent(n)
        # recurse to factor the not necessarily prime factor 
        result.extend(factors(factor)) 
        n //= factor
    if sort: return sorted(result)
    return result

def num_factors(n):
    """Input: A natural number n.
       Output: The number of distinct factors of n."""
    return len(list(set(factors(n))))

def factorization(n):
    """Input: A natural number n.
       Output: The prime factorization of n."""
    factors = {}
    for p in primefactors(n):
        try:
            factors[p] += 1
        except KeyError:
            factors[p] = 1
    return factors

def main():

    # Add tests

    assert(num_factors(12) == 2)
    assert(gcd(12, 30) == 6)

if __name__ == '__main__':
    main()
