import time
from scipy.special import binom as C

def combinatoric_selections():
    """Input: None.
       Output: The number of values of n for which nCr > 10**6."""
    return len([C(n, r) for n in range(1, 101) for r in range(n) if C(n, r) > 10 ** 6])

def main():
    
    t0 = time.time()
    ans = combinatoric_selections()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
