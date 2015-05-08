import time
from math import log10

def square_root_convergents():
    """Input: None.
       Output: The number of fractions that contain a numerator
               with more digits than the denominator in the first
               one-thousand expansions of the approximation of 2**0.5
               by 1 + 1/(2 + 1/(2 + 1/(2 +...)))"""
    n0 = 1
    d0 = 1
    S = 2
    n1 = 3
    d1 = 2
    count = 0
    for i in range(998):
        n = n0 * n1 + 2 * d0 * d1
        d = n0 * d1 + n1 * d0
        n1 = n
        d1 = d
        if int(log10(n)) + 1 > int(log10(d)) + 1: count += 1
    return count

def main():
    
    t0 = time.time()
    ans = square_root_convergents()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
