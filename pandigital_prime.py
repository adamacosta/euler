import time
from itertools import permutations
from math import factorial
from euler import is_prime

def largest_pandigital_prime():
    """Input: None.
       Output: The largest n-digit pandigital prime."""
    digits = list(map(str, reversed(range(1, 8))))
    for i in list(map(int, digits)):
        gen = permutations(digits)
        for j in range(factorial(i)):
            result = int(''.join(next(gen)))
            if is_prime(result):
                return result
        digits.remove(str(i))

t0 = time.time()
ans = largest_pandigital_prime()
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
