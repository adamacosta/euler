import time
from euler import cat, is_prime, primes

def prime_pair_sets():
    """Input: None.
       Output: The lowest sum for five primes for which the
               concatenation of any two is primes."""
    ps = primes(10000)
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            if not is_prime(cat([ps[i], ps[j]])): continue
            if not is_prime(cat([ps[j], ps[i]])): continue
            for k in range(j + 1, len(ps)):
                if not is_prime(cat([ps[i], ps[k]])): continue
                if not is_prime(cat([ps[j], ps[k]])): continue
                if not is_prime(cat([ps[k], ps[i]])): continue
                if not is_prime(cat([ps[k], ps[j]])): continue
                for l in range(k + 1, len(ps)):
                    if not is_prime(cat([ps[i], ps[l]])): continue
                    if not is_prime(cat([ps[j], ps[l]])): continue
                    if not is_prime(cat([ps[k], ps[l]])): continue
                    if not is_prime(cat([ps[l], ps[i]])): continue
                    if not is_prime(cat([ps[l], ps[j]])): continue
                    if not is_prime(cat([ps[l], ps[k]])): continue
                    for m in range(l + 1, len(ps)):
                        if not is_prime(cat([ps[i], ps[m]])): continue
                        if not is_prime(cat([ps[j], ps[m]])): continue
                        if not is_prime(cat([ps[k], ps[m]])): continue
                        if not is_prime(cat([ps[l], ps[m]])): continue
                        if not is_prime(cat([ps[m], ps[i]])): continue
                        if not is_prime(cat([ps[m], ps[j]])): continue
                        if not is_prime(cat([ps[m], ps[k]])): continue
                        if not is_prime(cat([ps[m], ps[l]])): continue
                        return sum([ps[i], ps[j], ps[k], ps[l], ps[m]])
    
def main():

    t0 = time.time()
    ans = prime_pair_sets()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
