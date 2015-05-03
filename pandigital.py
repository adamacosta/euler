import time

def pandigital(n):
    """Input: A natural number n >= 9.
    Output: The sum of all products whose multiplicand/
    multiplier/product sequence is pandigital."""
    products = set([])
    digits = set([i for i in range(1, n + 1)])
    max_num = 0
    for i in range(n, 0, -1):
        max_num += i * 10 ** (i - 1)
    max_num = int(''.join([c for c in str(max_num)[:n // 2]]))
    for i in range(max_num, 1, -1):
        for j in range(1, max_num // i):
            if set([int(c) for c in str(i) + str(j) + str(i * j)]) == digits:
                products.add(i * j)
    return sum(products)

n = 9

t0 = time.time()
ans = pandigital(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
