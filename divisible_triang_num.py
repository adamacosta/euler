import time
from math import ceil, log
from euler_utils.integer import divisors

def high_div_trian_num(n):
    """Input: an integer n.
    Output: the first triangular number with greater
    than n divisors."""
    n = ceil(n * log(n))
    while True:
        if n % 2:
            n_div = len(divisors(n)) * len(divisors((n + 1) // 2))
        else:
            n_div = len(divisors(n // 2)) * len(divisors(n + 1))
        if n_div > 500:
            return n * (n + 1) // 2
        n += 1

def main():

    n_divisors = 500

    t0 = time.time()
    ans = high_div_trian_num(n_divisors)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
