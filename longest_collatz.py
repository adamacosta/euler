import time

# Generates a Collatz sequence starting with num
def collatz_generator(num):
    while num != 1:
        num = 3 * num + 1 if num % 2 else num // 2
        yield num

def find_longest_collatz(n):
    """Input: Upper limit for the starting number.
    Output: Starting number of the longest Collatz sequence."""
    max_len = 1
    max_start = 0
    for i in range(n // 2, n):
        new_len = 1
        new_gen = collatz_generator(i)
        while next(new_gen) != 1:
            new_len += 1
        if new_len > max_len:
            max_len = new_len
            max_start = i
    return max_start

num = 1000000

t0 = time.time()
ans = find_longest_collatz(num)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
