from math import sqrt, ceil, log
import time

def num_divisors(n):
    """Input: an integer n.
    Output: the number of divisors of n."""
    # Every number is divisble by 1
    result = 1
    # Every number is divisble by itself
    if n > 1:
        result += 1
    for i in range(2, ceil(sqrt(n))):
        # Take advantage of symmetry of divisors
        if n % i == 0:
            result += 2
    return result

def high_div_trian_num(num):
    """Input: an integer num.
    Output: the first triangular number with greater
    than num divisors."""
    n = ceil(num * log(num))
    while True:
        if n % 2:
            n_div = num_divisors(n) * num_divisors((n + 1) // 2)
        else:
            n_div = num_divisors(n // 2) * num_divisors(n + 1)
        if n_div > 500:
            return n * (n + 1) // 2
        n += 1

n_divisors = 500

t0 = time.time()
ans = high_div_trian_num(n_divisors)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
