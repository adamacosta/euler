import time
from euler import digit_sum

def max_digit_sum(a, b):
    """Input: Two natural numbers a and b.
       Output: The maximum digit sum of any number a ** b for
               a and b less than the inputs."""
    return max([digit_sum(i**j) for i in range(1, a) for j in range(1, b)])

def main():

    a, b = 100, 100
    
    t0 = time.time()
    ans = max_digit_sum(a, b)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
