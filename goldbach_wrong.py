import time
from euler import is_prime, primes
from math import sqrt

def smallest_not_goldbach():
    """Input: None.
       Output: The smallest odd composite number that cannot be
               written as the sum of a prime and twice a square."""
    ps = primes(10000)
    for c in range(35, 99999, 2):
        if is_prime(c):
            continue
        for p in ps:
            goldbach = False
            if p > c - 2:
                break
            if sqrt((c - p) / 2).is_integer():
                goldbach = True
                break
        if not goldbach:
            return c

def main():
    
    t0 = time.time()
    ans = smallest_not_goldbach()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
