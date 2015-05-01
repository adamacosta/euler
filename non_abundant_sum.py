import time
from math import sqrt, ceil

def sum_divisors(n):
    """Input: An integer n > 1.
    Output: The sum of all the divisors of n."""
    result = 1
    root = sqrt(n)
    for i in range(2, ceil(root)):
        if not n % i:
            result += i + n // i
    if root == ceil(root):
        result += int(root)
    return result

def non_abundant_sum():
    """Input: None.
    Output: The sum of all positive integers that cannot
    be written as the sum of two abundant numbers."""
    max_num = 28123
    all_nums = set(range(1, max_num + 1))
    abundants = [i for i in range(12, 28112) if sum_divisors(i) > i]
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            if abundants[i] + abundants[j] > max_num:
                break
            all_nums.discard(abundants[i] + abundants[j])
    return sum(all_nums)

t0 = time.time()
ans = non_abundant_sum()
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
