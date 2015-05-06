import time
from math import sqrt, ceil
from euler import primes

def consecutive_distinct_factors():
    """Input: None.
       Output: The first consecutive sequence of four integers
               that have four distinct factors."""
    nmax = 500000
    start = 2**2 * 3**2 * 5**2 * 7**2
    ps = primes(ceil(sqrt(nmax)))
    facts = [0 for i in range(nmax + 1)]
    for p in ps:
        for i in range(p, nmax + 1, p): facts[i] += 1
    for i in range(start, nmax + 1):
        if facts[i]==4 and facts[i+1]==4 and facts[i+2]==4 and facts[i+3]==4:
            return i

def main():
    
    t0 = time.time()
    ans = consecutive_distinct_factors()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
