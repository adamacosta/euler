from itertools import chain, permutations
from math import factorial, floor, log10
from functools import reduce
from collections import deque

# Utilities for processing and permuting strings and digits

letter_vals = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
               'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
               'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def is_palindrome(s):
    """Input: A string s.
       Output: Whether or not s is a palindrome."""
    return str(s)[:len(str(s))//2] == str(s)[-(len(str(s))//2):][::-1]

def reverse(n):
    """Input: A number n.
       Output: The same number reversed."""
    return int(str(n)[::-1])

def is_pandigital(n):
    """Input: An integer n.
       Output: Whether or not n is n-digit pandigital."""
    if len(str(n)) == 10:
        digits = set(map(str, list(range(0, 10))))
    else:
        digits = set(map(str, list(range(1, len(str(n)) + 1))))
    return set(str(n)) == digits

def is_permutation(n, m):
    """Input: Two numbers.
       Output: Whether or not they are permutations of the same digits."""
    return len(str(n)) == len(str(m)) and set(str(n)) == set(str(m))

def digit_permutations(n):
    """Input: A natural number n.
       Output: Permutations of the digits of n."""
    gen = permutations(str(n))
    for i in range(factorial(n)):
        yield int(''.join(next(gen)))

def comb_btw(i, j):
    """Input: Two digits i and j.
       Output: All combinations of digits between i and j."""
    for k in range(1, j - i + 2):
        gen = combinations([n for n in range(i, j + 1)], k)
        for l in range(factorial(j-i+1)//factorial(k)//factorial(j-i-k+1)):
            yield list(next(gen))

def get_digits(n):
    """Input: A natural number n.
       Output: A list of the digits of n."""
    result = deque([])
    for i in range(1, floor(log10(n)) + 1):
        result.appendleft(n % 10)
        n -= n % 10
        n //= 10
    result.appendleft(n)
    return list(result)

def digit_sum(n):
    """Input: A natural number n.
       Output: The sum of the digits in n."""
    return reduce(lambda x, y: x + y, get_digits(n))

def dig_rep(n, inds):
    """Input: A natural number n and list of indices.
       Output: Permutations of n with the indexed digits replaced."""
    digits = get_digits(n)
    for i in inds:
        digits[i] = 0
    result = 0
    for i in range(len(digits)):
        result += digits[i] * 10 ** (len(digits) - i - 1)
    for i in range(9):
        for j in inds:
            result += 10 ** (len(digits) - j - 1)
        yield result

def cat(s):
    """Input: A list of numbers.
       Output: The concatenation of the numbers."""
    return int(reduce(lambda x, y: x + y, [str(i) for i in s]))

def all_cats(s):
    """Input: A list of numbers.
       Output: All concatenations of two numbers."""
    return list(chain.from_iterable([[cat([i, j]), cat([j, i])] for i, j in combinations(s, 2)]))

def main():

    # Add tests

    assert(is_pandigital(123456789))
    assert(not is_pandigital(12345679))

    assert(is_palindrome(12345678987654321))
    assert(not is_palindrome(12345678654321))

    assert(reverse(123456789) == 987654321)

    assert(is_permutation(123456789, 456123789))
    assert(not is_permutation(12345, 45678))

if __name__ == '__main__':
    main()
