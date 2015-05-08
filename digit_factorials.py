import time
from euler_utils.primes import primes

def rotations(n):
    """Input: A natural number n.
    Output: A list of all rotations of the digits of n,
    except the original ordering of n."""
    digits = [i for i in str(n)]
    if '2' in digits or '4' in digits or '5' in digits or '6' in digits \
       or '8' in digits:
        return [2]
    result = []
    start = 1
    for j in range(len(digits) - 1):
        new = []
        for i in range(len(digits)):
            new.append(digits[start])
            start = (start + 1) % len(digits)
        result.append(int(''.join(new)))
        start = (start + 1) % len(digits)
    return result

def circular_primes(n):
    """Input: A natural number n.
    Output: The number of circular primes less than n."""
    pos = set(primes(n))
    result = 13
    while len(pos) != 0:
        num = pos.pop()
        new = set(rotations(num))
        if sum([item in pos for item in new]) == len(new):
            result += len(new) + 1
            pos ^= new
    return result

def main():

    n = 1000000

    t0 = time.time()
    ans = circular_primes(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
