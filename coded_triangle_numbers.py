import time
from euler import triangles, letter_vals

def coded_triangles(words):
    """Input: A list of words.
       Output: The number of words that are coded triangle numbers.
               That is, the sum of the numerical values of each letter
               as a position in the alphabet is a triangle number."""
    t = set(triangles)
    return sum([sum([letter_vals[c] for c in word]) in t for word in words])

def main():
    words = open("words.txt").read()
    words = words.replace('"', '').split(',')

    t0 = time.time()
    ans = coded_triangles(words)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
