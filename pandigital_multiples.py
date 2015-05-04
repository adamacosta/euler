import time

def cat_prod(n, m):
    """Input: An integer n and a limit m.
    Output: The concatenated product of n with 1...m"""
    return int(''.join([str(n * i) for i in range(1, m + 1)]))

def is_pandigital(n):
    """Input: An integer n.
    Output: Whether or not n is pandigital."""
    return len(str(n)) == 9 and set(str(n)) == set('123456789')

def greatest_pandigital():
    """Input: None.
    Output: The greatest pandigital number that can be
    expressed as the concatenated product of some number
    with single digits."""
    result = 918273645
    for i in range(9000, 9876):
        for j in range(1, 10):
             tmp = cat_prod(i, j)
             result = max(tmp, result) if is_pandigital(tmp) else result
    return result

t0 = time.time()
ans = greatest_pandigital()
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
