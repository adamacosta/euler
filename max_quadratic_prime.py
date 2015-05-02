import time

def get_primes(n): 
    numbers = list(range(3, n + 1, 2))
    half =  n // 2
    initial = 4
    for step in range(3, n + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)
        if initial > half:
            return [2] + [i for i in numbers if i]

def max_quadratic_prime(n):
    """Input: A natural number n.
    Output: Product of coefficients [a, b] of the
    quadratic formula n^2 + an + b = p for which
    p is prime for the maximum consecutive n, starting at 0,
    with constraints |a| < n and |b| < n."""
    # Clearly, b must be prime
    pos = set(get_primes(n ** 2))
    bs = [i for i in pos if i < 1000]
    # a = p - b - 1 for some prime p, so abs(a) must be prime
    all_as = [i for i in range(-999, 1000) if abs(i) in pos]
    max_count = 0
    result = 0
    for b in bs:
        # Since p = 1 + a + b must be >= 2, we get 1 + a + b >= 2,
        # or a >= 1 - b
        for a in [i for i in all_as if i >= 1 - b]:
            count = 0
            for k in range(b - a):
                if k ** 2 + k * a + b not in pos:
                    break
                count += 1
            if count > max_count:
                max_count = count
                result = a * b
    return result

n = 1000

t0 = time.time()
ans = max_quadratic_prime(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
