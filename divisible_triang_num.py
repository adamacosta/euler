import time
from math import ceil, log
from euler import divisors

def high_div_trian_num(num):
    """Input: an integer num.
    Output: the first triangular number with greater
    than num divisors."""
    n = ceil(num * log(num))
    while True:
        if n % 2:
            n_div = len(divisors(n)) * len(divisors((n + 1) // 2))
        else:
            n_div = len(divisors(n // 2)) * len(divisors(n + 1))
        if n_div > 500:
            return n * (n + 1) // 2
        n += 1

n_divisors = 500

t0 = time.time()
ans = high_div_trian_num(n_divisors)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
