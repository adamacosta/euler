import time

def digit_powers(n):
    """Input: A natural number n.
    Output: The sum of all numbers that can be written
    as the sum of nth powers of their digits."""
    result = 0
    for i in range(2 ** n, n * 9 ** n):
        if i == sum([int(j) ** n for j in str(i)]):
            result += i
    return result

def main():

    n = 5

    t0 = time.time()
    ans = digit_powers(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
