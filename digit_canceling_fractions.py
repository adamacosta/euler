import time

def gcd(n, m):
    """Input: Two integers n and m.
    Output: The greatest common divisor of n and m."""
    if m == 0:
        return n
    return gcd(m, n % m)

def digit_cancelling_fractions():
    """Input: None.
    Output: The value of the denominator of the product
    of all digit cancelling fractions less than 1 with
    at most 2 digits in the numerator and denominator."""
    min_num = 10
    max_num = 99
    numerator = 1
    denominator = 1
    for i in range(min_num, max_num + 1):
        for j in range(i * 2, max_num + 1):
            i0 = int(str(i)[0])
            i1 = int(str(i)[1])
            j0 = int(str(j)[0])
            j1 = int(str(j)[1])
            if i1 == 0 and j1 == 0:
                continue
            if (i/i0) == (j/j0):
                continue
            if j0 == 0:
                continue
            if ((i/j)==(i0/j0) and i1==j1) or ((i/j)==(i1/j0) and i0==j1):
                numerator *= i
                denominator *= j
            if j1 == 0:
                continue
            if ((i/j)==(i0/j1) and i1==j0) or ((i/j)==(i1/j1) and i0==j0):
                numerator *= i
                denominator *= j
    return denominator // gcd(numerator, denominator)

t0 = time.time()
ans = digit_cancelling_fractions()
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
