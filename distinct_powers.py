import time

def distinct_powers(n):
    """Input: A natural number n.
    Output: The number of distinct powers a^b,
    for 2 <= a <= n and 2 <= b <= n"""
    pows = set([])
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            pows.add(a**b)
    return len(pows)

n = 100

t0 = time.time()
ans = distinct_powers(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
