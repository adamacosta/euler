from math import ceil, log
import time

def nth_prime(n):
    nmax = ceil(n * log(n * log(n)))
    numbers = list(range(3, nmax + 1, 2))
    half =  nmax // 2
    initial = 4
    for step in range(3, nmax + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)
        if initial > half:
            return ([2] + [i for i in numbers if i])[n - 1]

num = 10001

t0 = time.time()
ans = nth_prime(num)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
