import time
from euler_utils.digits import is_palindrome

def largest_palindromic_product(n=3):
    max_num = int(str(9) * n)
    min_num = 10 ** (n - 1)
    max_pal = 0
    for i in range(max_num - 9, min_num, -11):
        for j in range(max_num, min_num, -1):
            if is_palindrome(str(i * j)) and i * j > max_pal:
                max_pal = i * j
    return max_pal

def main():

    t0 = time.time()
    ans = largest_palindromic_product()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(elapsed) + " seconds")

if __name__ == '__main__':
    main()
