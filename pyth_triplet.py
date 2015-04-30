from math import sqrt
import time

def find_pyth(n):
    for a in range(1, n // 3):
        for b in range(a + 1, n // 2):
            c = sqrt(a**2 + b **2)
            if a + b + c == 1000:
                return int(a * b * c)

num = 1000

t0 = time.time()
ans = find_pyth(num)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
