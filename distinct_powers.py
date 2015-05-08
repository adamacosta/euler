import time

def distinct_powers(n):
    """Input: A natural number n.
    Output: The number of distinct powers a^b,
    for 2 <= a <= n and 2 <= b <= n"""
    return len(set([a ** b for a in range(2, n + 1) for b in range(2, n + 1)]))

def main():

    n = 100

    t0 = time.time()
    ans = distinct_powers(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
