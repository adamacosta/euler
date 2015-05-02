import time

def sum_spiral_diagonal(n):
    """Input: A natural number n.
    Output: The sum of the diagonals in an n x n spiral"""
    num = 1
    result = 1
    for step in range(2, n, 2):
        for arm in range(4):
            num += step
            result += num
    return result

n = 1001

t0 = time.time()
ans = sum_spiral_diagonal(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
