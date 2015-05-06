import time

def self_powers():
    """Input: None.
       Output: The last ten digits of 1^2 + ... + 1000^1000."""
    return sum([i**i for i in range(1, 1001)]) % 10**10

def main():
    
    t0 = time.time()
    ans = self_powers()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
