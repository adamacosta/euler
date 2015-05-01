import time
from itertools import permutations

def nth_permutation(s, n):
    """Input: A string s and a natural number n.
    Output: The nth lexicographic permutation of s."""
    perms = permutations(s)
    result = None
    for i in range(n):
        result = next(perms)
    return ''.join(result)

s = '0123456789'
n = 1000000

t0 = time.time()
ans = nth_permutation(s, n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
