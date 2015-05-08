import time
from numpy import binary_repr
from euler_utils.digits import is_palindrome

def double_base_palindromes(n):
    """Input: A natural number n.
    Output: The sum of all numbers less than n that
    are palindromic both in decimal and binary."""
    # Start with all odd single-digit numbers, then
    # add 33 and 99, the only palindromic two-digit numbers
    # that are also palindromic in binary
    result = 157
    for i in range(101, n, 2):
        # Only odd numbers are palindromic in binary
        if is_palindrome(str(i)) and is_palindrome(binary_repr(i)):
            result += i
    return result

def main():

    n = 1000000

    t0 = time.time()
    ans = double_base_palindromes(n)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
