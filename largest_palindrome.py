import time

def is_palindrome(s):
    return s == s[::-1]

def largest_palindromic_product(n=3):
    max_num = int(str(9) * n)
    min_num = 10 ** (n - 1)
    max_pal = 0
    for i in range(max_num - 9, min_num, -11):
        for j in range(max_num, min_num, -1):
            if is_palindrome(str(i * j)) and i * j > max_pal:
                max_pal = i * j
    return max_pal

t0 = time.time()
answer = largest_palindromic_product()
t1 = time.time()
elapsed = t1 - t0

print(answer)
print("Took " + str(elapsed) + " seconds")
