from math import sqrt, ceil

def is_prime(n):
    imax = sqrt(n)
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while n % i != 0 and i <= imax:
        i += 2
    return i > imax

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

def max_prime_factor(n):
    primes = get_primes(ceil(sqrt(n)))
    for i in primes:
        if n % i == 0:
            if is_prime(n // i):
                return n // i
            else:
                return max_prime_factor(n // i)
    return n

test_num = 600851475143

print(max_prime_factor(test_num))

