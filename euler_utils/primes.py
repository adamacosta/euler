import numpy as np

# Prime number generators and utility functions

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

def prime_generator(n):
    """Input: A natural number n.
       Output: An iterator returning all primes less than n."""
    ps = primes(n)
    for i in range(len(ps)):
        yield ps[i]

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
            if pow(a, 2 ** i * d, n) == n - 1: return False
        return True 
    
    for i in range(trials):
        a = np.random.randint(2, n - 1)
        if try_composite(a): return False
    return True

def all_primes(n):
    """Input: A list of numbers.
       Output: Whether all numbers are prime."""
    return len(n) == sum([is_prime(i) for i in n])

def main():

    # Add tests

    assert(is_prime(13))
    assert(not is_prime(12))

if __name__ == '__main__':
    main()
