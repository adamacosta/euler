import time
import numpy as np
from collections import Counter

A = np.array([[-1,2,2],
              [-2,1,2],
              [-2,2,3]])

B = np.array([[1,2,2],
              [2,1,2],
              [2,2,3]])

C = np.array([[1,-2,2],
              [2,-1,2],
              [2,-2,3]])

def berggren(seeds):
    """Input: A list of Pythagorean triples.
    Output: Three children Pythagorean triples generated according to
    Berggren's three matrices."""
    result = []
    for b in seeds:
        result.extend([list(np.dot(A,b)),list(np.dot(B,b)),list(np.dot(C,b))])
    return result

def primitive_pythagorean_triples():
    """Input: None.
    Output: All primitive Pythagoren triples with sums <= 1000."""
    result = [[3,4,5]]
    for i in range(5):
        result.extend(berggren(result))
    return [i for i in result if sum(i) <= 1000]

def pythagorean_triples():
    """Input: None.
    Output: All Pythagorean triples with sums <= 1000."""
    triples = primitive_pythagorean_triples()
    for prim in triples:
        if sum(prim) < 1000:
            i = 2
            while True:
                not_prim = list(i * np.array(prim))
                if sum(not_prim) < 1000:
                    triples.append(not_prim)
                    i += 1
                else:
                    break
    return [list(i) for i in set(tuple(i) for i in triples)]

def count_triple_sums(triples):
    """Input: None.
    Output: The most common sum of all Pythagorean triples with a
    sum less than 1000."""
    return [sum(i) for i in triples]

def most_common(nums):
    """Input: A list of numbers.
    Output: The most common number."""
    return Counter(nums).most_common(1)[0][0]

t0 = time.time()
ans = most_common(count_triple_sums(pythagorean_triples()))
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
