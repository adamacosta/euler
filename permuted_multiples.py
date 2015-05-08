import time
from euler import is_permutation

def permuted_multiples():
    """Input: None.
       Output: The smallest positive integer x such that 2x,
               3x, 4x, 5x, and 6x are permutations of each other."""
    n = 125874
    while True:
        n += 1
        if is_permutation(n, 2 * n):
            if is_permutation(n, 3 * n):
                if is_permutation(n, 4 * n):
                    if is_permutation(n, 5 * n):
                        if is_permutation(n, 6 * n):
                            return n

def main():
    
    t0 = time.time()
    ans = permuted_multiples()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
