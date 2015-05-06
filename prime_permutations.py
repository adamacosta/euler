import time
from euler import cat, is_permutation, primes

def prime_permutations():
    """Input: None.
       Output: The concatenation of three 4-digit numbers
               that are prime permutations."""
    ps = primes(10000)
    ps = set(ps[ps > 1487])
    for p in ps:
        if p + 3330 in ps and p + 6660 in ps:
            if is_permutation(p, p + 3330) and is_permutation(p, p + 6660):
                return cat([p, p + 3330, p + 6660])

def main():
    
    t0 = time.time()
    ans = prime_permutations()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
