import time
from math import sqrt, ceil
from euler_utils.primes import is_prime, primes

def max_prime_factor(n):
    ps = primes(ceil(sqrt(n)))
    for p in ps:
        if not n % p:
            if is_prime(n // p):
                return n // p
            else:
                return max_prime_factor(n // p)
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
