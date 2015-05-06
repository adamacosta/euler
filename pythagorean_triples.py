import time
from collections import Counter
from euler import pythagorean_triples

def count_triple_sums(triples):
    """Input: None.
       Output: The most common sum of all Pythagorean triples with a
       sum less than 1000."""
    return [sum(i) for i in triples]

def most_common(nums):
    """Input: A list of numbers.
       Output: The most common number."""
    return Counter(nums).most_common(1)[0][0]

def main():

    n = 1000

    t0 = time.time()
    ans = most_common(count_triple_sums(pythagorean_triples(n)))
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
