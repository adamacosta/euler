import time

def get_primes(n):
    """Input: A natural number n > 100.
    Output: All the primes p such that 100 < p < n."""
    numbers = list(range(3, n + 1, 2))
    half =  n // 2
    initial = 4
    for step in range(3, n + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)
        if initial > half:
            return [i for i in numbers if i > 100]

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
    pos = set(get_primes(n))
    result = 13
    while len(pos) != 0:
        num = pos.pop()
        new = set(rotations(num))
        if sum([item in pos for item in new]) == len(new):
            result += len(new) + 1
            pos ^= new
    return result

n = 1000000

t0 = time.time()
ans = circular_primes(n)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
