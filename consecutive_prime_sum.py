import time
from euler import smallprimes as ps

def consecutive_prime_sum():
    """Input: None.
       Output: The prime less than one million that can be written
               as the sum of the most consecutive primes."""
    test = set(ps)
    max_count = 0
    result = 0
    vals = [0 for i in range(550)]
    for i in range(550):
        for j in range(i + 1, 550):
            vals[i] += ps[j]
            if j - i > max_count:
                if vals[i] + ps[i] in test:
                    max_count = j - i
                    result = vals[i] + ps[i]
    return result

def main():
    
    t0 = time.time()
    ans = consecutive_prime_sum()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
