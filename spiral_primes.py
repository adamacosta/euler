import time
from euler import is_prime

def spiral_primes():
    """Input: None.
       Output: The spiral size for which the ratio of prime/composite
               numbers on the main diagonal falls below 10%."""
    step = 6
    n = 49
    ps = 8
    while ps / (step + step + 1) > 0.1:
        step += 2
        ps += sum(list(map(is_prime, [n + step * i for i in range(1, 4)])))
        n += 4 * step
    return step + 1

def main():
    
    t0 = time.time()
    ans = spiral_primes()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
