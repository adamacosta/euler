import time
from math import sqrt, ceil
from euler import is_prime, sundaram

def max_prime_factor(n):
    primes = sundaram(ceil(sqrt(n)))
    for i in primes:
        if n % i == 0:
            if is_prime(n // i):
                return n // i
            else:
                return max_prime_factor(n // i)
    return n

def main():
    
    n = 600851475143
    
    t0 = time.time()
    ans = max_prime_factor(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
