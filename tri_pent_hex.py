import time
from euler import pentagon_numbers, hexagon_numbers

def tri_pent_hex():
    """Input: None.
       Output: The next triangle number that is also a pentagon
               number and hexagon number after 40755."""
    h = hexagon_numbers(100000)[143:]
    p = set(pentagon_numbers(100000)[165:])
    for n in h:
        if n in p:
            return n

def main():
    
    t0 = time.time()
    ans = tri_pent_hex()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
