import time

def get_primes_over_five(n):
    """Input: A natural number n.
    Output: All primes less than n, except 2 and 5."""
    numbers = list(range(3, n + 1, 2))
    half =  n // 2
    initial = 4
    for step in range(3, n + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)
        if initial > half:
            return [i for i in numbers if i][2:]

def max_reciprocal_cycle(n):
    """Input: A natural number n.
    Output: The value of d < n for which 1 / d has the
    maximum length recurring cycle."""
    ds = get_primes_over_five(n)
    cycles = []
    # Every cycling rational number is expressible as
    # 1 / d = k / 10^n - 1, where n = len(k), so k = (10^n-1) / d
    # Thus, d must be a prime factor of 10^n - 1
    for d in ds:
        for i in range(1, d):
            if 10 ** i % d == 1:
                cycles.append(i)
                break
    return ds[cycles.index(max(cycles))]

n = 1000

t0 = time.time()
ans = max_reciprocal_cycle(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
