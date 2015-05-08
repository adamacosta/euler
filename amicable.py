import time
from math import ceil, sqrt
from euler_utils.integer import sum_divisors

def sum_amicable(n):
    """Input: A natural number n.
    Output: The sum of all amicable numbers less than n."""
    result = 0
    for i in range(2, n):
        for j in range(i + 1, n):
            if sum_divisors(i) == j and sum_divisors(j) == i:
                result += i + j
    return result

def main():

    num = 10000

    t0 = time.time()
    ans = sum_amicable(num)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
