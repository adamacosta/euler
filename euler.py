import random
import numpy as np
from math import sqrt, ceil, log

triangles = [1,3,6,10,15,21,28,36,45,55,66,78,91,105,120,136,153,171,190,210,
	     231,253,276,300,325,351,378,406,435,465,496,528,561,595,630,666,
	     703,741,780,820,861,903,946,990,1035,1081,1128,1176,1225,1275,
	     1326,1378,1431,1485,1540,1596,1653,1711,1770,1830,1891,1953,2016,
	     2080,2145,2211,2278,2346,2415,2485,2556,2628,2701,2775,2850,2926,
	     3003,3081,3160,3240,3321,3403,3486,3570,3655,3741,3828,3916,4005,
	     4095,4186,4278,4371,4465,4560,4656,4753,4851,4950,5050]

letter_vals = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
               'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
               'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def is_prime(n):
    """Miller-Rabin primality test.
       Input: A natural number n.
       Output: Whether or not n is prime with high probability."""
    trials = 5
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        q, r = divmod(d, 2)
        if r == 1:
            break
        s += 1
        d = q
    assert(2**s * d == n - 1)

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True 
    
    for i in range(trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
    return True

def is_palindrome(s):
    """Input: A string s.
       Output: Whether or not s is a palindrome."""
    return s == s[::-1]

def is_pandigital(n):
    """Input: An integer n.
       Output: Whether or not n is n-digit pandigital."""
    if len(str(n)) == 10:
        digits = set(map(str, list(range(0, 10))))
    else:
        digits = set(map(str, list(range(1, len(str(n)) + 1))))
    return set(str(n)) == digits

def divisors(n):
    """Input: An integer n.
       Output: The divisors of n."""
    # Every number is divisble by 1
    result = [1]
    # Every number is divisble by itself
    if n > 1:
        result.append(n)
    for i in range(2, ceil(sqrt(n))):
        # Take advantage of symmetry of divisors
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result

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

def primitive_pythagorean_triples():
    """Input: None.
       Output: All primitive Pythagoren triples with sums <= 1000."""
    result = [[3,4,5]]
    for i in range(5):
        result.extend(berggren(result))
    return [i for i in result if sum(i) <= 1000]

def pythagorean_triples():
    """Input: None.
       Output: All Pythagorean triples with sums <= 1000."""
    triples = primitive_pythagorean_triples()
    for prim in triples:
        if sum(prim) < 1000:
            i = 2
            while True:
                not_prim = list(i * np.array(prim))
                if sum(not_prim) < 1000:
                    triples.append(not_prim)
                    i += 1
                else:
                    break
    return [list(i) for i in set(tuple(i) for i in triples)]
