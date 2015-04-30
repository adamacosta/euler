from math import log, floor

def get_primes(n): 
    numbers = list(range(3, n + 1, 2))
    half =  n // 2
    initial = 4
    for step in range(3, n + 1, 2):
        for i in range(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)
        if initial > half:
            return [2] + [i for i in numbers if i]

def lcm(n):
    primes = get_primes(n)
    not_primes = [i for i in range(4, n + 1) if not i in primes]
    mults = []
    for j in range(len(primes)):
        for i in reversed(not_primes):
            if log(i, primes[j]) == floor(log(i, primes[j])):
                primes[j] = 1
                mults.append(i)
                break
    ans = 1
    for i in primes:
        ans *= i
    for j in mults:
        ans *= j
    return ans

print(lcm(20))
