import time

def n_digit_fib(n):
    """Input: A natural number n.
    Output: The first Fibonacci number with n digits."""
    f1 = 1
    f2 = 2
    fib = 0
    i = 3
    while fib < 10 ** (n - 1):
        fib = f1 + f2
        f1 = f2
        f2 = fib
        i += 1
    return i

n = 1000

t0 = time.time()
ans = n_digit_fib(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
