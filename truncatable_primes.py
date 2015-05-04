import time
import random
from euler import sundaram, is_prime, all_primes

def truncations(n):
    """Input: A natural number n.
       Output: All left and right truncations of n."""
    result = []
    s = str(n)
    for i in range(1, len(s)):
        result.append(int(''.join(s[i:])))
        result.append(int(''.join(s[:i])))
    return result

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
