import time
import numpy as np
from euler import is_prime, dig_rep, comb_btw, smallprimes as ps

def prime_digit_replacement(n):
    """Input: None.
       Output: The smallest prime that is in a family of n that can be
               formed by replacing digits."""
    for p in ps:
        al = [[i for i in dig_rep(p, l)] for l in comb_btw(0, len(str(p)) - 1)]
        for a in al:
            if sum(map(is_prime, a)) == n:
                return p

def main():

    n = 7
    
    t0 = time.time()
    ans = prime_digit_replacement(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
