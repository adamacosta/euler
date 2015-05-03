import time
import random

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

def is_prime(n):
    """Miller-Rabin primality test.
    Input: A natural number n.
    Output: Whether or not n is prime with high probability."""
    num_trials = 5
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True 
    
    for i in range(num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
    return True

def truncations(n):
    """Input: A natural number n.
    Output: All left and right truncations of n."""
    result = []
    s = str(n)
    for i in range(1, len(s)):
        result.append(int(''.join(s[i:])))
        result.append(int(''.join(s[:i])))
    return result

def all_primes(n):
    """Input: A list of numbers.
    Output: Whether all numbers are prime."""
    return len(n) == sum([is_prime(i) for i in n])

def truncatable_primes():
    """Input: None.
    Output: The sum of all truncatable prime numbers."""
    result = []
    primes = [i for i in sundaram(1000000) if i > 11]
    for p in primes:
        if all_primes(truncations(p)):
            result.append(p)
            if len(result) == 11:
                return sum(result)

t0 = time.time()
ans = truncatable_primes()
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
