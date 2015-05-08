import time
from euler import reverse, is_palindrome

def lychrels(n):
    """Input: A natural number n.
       Output: The number of Lychrel numbers estimated to
               exist less than n."""
    not_lychrel = 0
    for i in range(1, n):
        for j in range(50):
            i += reverse(i)
            if is_palindrome(i):
                not_lychrel += 1
                break
    return n - not_lychrel - 1

def main():

    n = 10000
    
    t0 = time.time()
    ans = lychrels(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
