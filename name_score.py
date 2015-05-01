import time
import pandas as pd

def name_score(s):
    """Input: s, a list of strings.
    Output: The lexicographic score of each string multiplied
    by its index when sorted."""
    total = 0
    ind = 1
    base = ord('A') - 1
    for word in sorted(s):
        score = 0
        for c in word:
            score += (ord(c) - base)
        total += ind * score
        ind += 1
    return total

filename = "names.txt"
names = list(pd.read_csv(filename).columns.values)

t0 = time.time()
ans = name_score(names)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
