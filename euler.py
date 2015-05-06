import random
import numpy as np
from numpy.random import randint
from math import sqrt, ceil, log, floor
from functools import reduce

letter_vals = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
               'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
               'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def primes(n):
    """Input: A natural number n.
       Output: An array of primes, p < n."""
    assert n >= 2
    sieve = np.ones(n / 2, dtype=np.bool)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i / 2]:
            sieve[i * i / 2::i] = False
    return np.r_[2, 2 * np.nonzero(sieve)[0][1::] + 1]

def bigprimes(n):
    """Input: A natural number n.
       Output: An array of primes, p < n.
               Faster than primes for n > 1000000."""
    sieve = np.ones(n / 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(floor(sqrt(n)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]

smallprimes = primes(1000000)
_smallprimes = set(smallprimes)

def is_prime(n, trials=5):
    """Miller-Rabin primality test.
       Input: A natural number n.
       Output: Whether or not n is prime with high probability."""
    if n == 1: return False
    if n == 2: return True
    if not n % 2: return False
    if n < 100000: return n in _smallprimes
    
    s = 0
    d = n - 1
    
    while True:
        q, r = divmod(d, 2)
        if r == 1:
            break
        s += 1
        d = q
    assert(2 ** s * d == n - 1)

    def try_composite(a):
        if pow(a, d, n) == 1: return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n-1: return False
        return True 
    
    for i in range(trials):
        a = randint(2, n - 1)
        if try_composite(a): return False
    return True

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

    y, c, m = randint(1, n), randint(1, n), randint(1, n)
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

def is_palindrome(s):
    """Input: A string s.
       Output: Whether or not s is a palindrome."""
    return s[:len(s)//2] == s[-len(s)//2:][::-1]

def is_pandigital(n):
    """Input: An integer n.
       Output: Whether or not n is n-digit pandigital."""
    if len(str(n)) == 10:
        digits = set(map(str, list(range(0, 10))))
    else:
        digits = set(map(str, list(range(1, len(str(n)) + 1))))
    return set(str(n)) == digits

def is_permutation(n, m):
    """Input: Two numbers.
       Output: Whether or not they are permutations of the same digits."""
    return len(str(n)) == len(str(m)) and set(str(n)) == set(str(m))

def cat(s):
    """Input: A list of numbers.
       Output: The concatenation of the numbers."""
    return int(reduce(lambda x, y: x + y, [str(i) for i in s]))

def sundaram(n):
    """Sieve of Sundaram.
       Input: A natural number n.
       Output: All primes numbers less than n."""
    numbers = list(range(3, n + 1, 2))
    half =  n // 2
    initial = 4
    for step in range(3, n + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)
        if initial > half:
            return [2] + [i for i in numbers if i]

def all_primes(n):
    """Input: A list of numbers.
       Output: Whether all numbers are prime."""
    return len(n) == sum([is_prime(i) for i in n])

def berggren(seeds):
    """Input: A list of Pythagorean triples.
       Output: Three children Pythagorean triples generated according to
       Berggren's three matrices."""
    A = np.array([[-1,2,2],
                  [-2,1,2],
                  [-2,2,3]])

    B = np.array([[1,2,2],
                  [2,1,2],
                  [2,2,3]])

    C = np.array([[1,-2,2],
                  [2,-1,2],
                  [2,-2,3]])
    result = []
    for b in seeds:
        result.extend([list(np.dot(A,b)),list(np.dot(B,b)),list(np.dot(C,b))])
    return result

def primitive_pythagorean_triples(n):
    """Input: A natural number n.
       Output: All primitive Pythagoren triples with sums <= n."""
    result = [[3,4,5]]
    for i in range(ceil(log(n))):
        result.extend(berggren(result))
    return [i for i in result if sum(i) <= n]

def pythagorean_triples(n):
    """Input: A natural number n.
       Output: All Pythagorean triples with sums <= n."""
    triples = primitive_pythagorean_triples(n)
    for prim in triples:
        if sum(prim) < n:
            i = 2
            while True:
                not_prim = list(i * np.array(prim))
                if sum(not_prim) < n:
                    triples.append(not_prim)
                    i += 1
                else:
                    break
    return [sorted(list(i)) for i in set(tuple(i) for i in triples)]

def triangle_numbers(n):
    """Input: A natural number n.
       Output: All triangle numbers up to n(n + 1)/2."""
    return list(np.arange(1, n + 1) * np.arange(2, n + 2) // 2)

def pentagon_numbers(n):
    """Input: A natural number n.
       Output: All pentagon numbers up to n(3n - 1)/2."""
    return list(np.arange(1, n + 1) * (3 * np.arange(1, n + 1) - 1) // 2)

def hexagon_numbers(n):
    """Input: A natural number n.
       Output: All hexagon numbers up to n(2n - 1)."""
    return list(np.arange(1, n + 1) * (2 * np.arange(1, n + 1) - 1))

def squarefree(n):
    """Input: A natural number n.
       Output: Squarefree numbers up to n."""
    return np.setdiff1d(np.arange(1, n), np.arange(1, floor(sqrt(n))) ** 2)
