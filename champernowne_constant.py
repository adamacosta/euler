import time
from functools import reduce

def champernowne():
    """Input: None.
       Output: d_1 x ... x d_1000000 for d_i in the string
               created by concatenating the positive integers.""" 
    s = ''.join(map(str, range(1, 185186)))
    return reduce(lambda x,y : x*y, [int(s[i]) for i in [10**k-1 for k in range(7)]])

def main():

    t0 = time.time()
    ans = champernowne()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
