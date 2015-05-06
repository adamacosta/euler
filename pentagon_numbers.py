import time
from euler import pentagon_numbers

def pentagon():
    """Input: None.
       Output: The minimum value D = |p_j - p_k| for which p_j, p_k,
               and D are all pentagon numbers."""
    p = pentagon_numbers(10000)
    ht = set(p)
    result = []
    for j in range(len(p)):
        for k in range(j, len(p)):
            if p[k] - p[j] in ht and p[j] + p[k] in ht:
                return abs(p[k] - p[j])

def main():
    
    t0 = time.time()
    ans = pentagon()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
