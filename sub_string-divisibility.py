import time
from itertools import permutations

def three_digits():
    """Input: None.
       Output: A list of all permutations of three digits
               drawn from the set {0,1,2,3,4,5,6,7,8,9}."""
    digits = list(map(str, range(10)))
    gen = permutations(digits, 3)
    return [''.join(next(gen)) for i in range(720)]
        
def substring_divisible_pandigitals():
    """Input: None.
       Output: The sum of all 0-9 pandigital numbers with the
               digit property 2 | d_2d_3d_4, 3 | d_3d_4d_5, etc."""
    digits = list(map(str, range(10)))
    result = [i for i in three_digits() if not int(i) % 17]
    divisors = [13,11,7,5,3,2]
    for i in range(6):
        for digit in digits:
            for j in range(len(result)):
                if digit in result[j]:
                    continue
                if not int(digit + result[j][:-(i+1)]) % divisors[i]:
                    result.append(digit + result[j])
        result = [n for n in result if len(n) == 4 + i]
    result = [digit + i for digit in digits for i in result if digit not in i]
    return sum([int(i) for i in result])

def main():
    
    t0 = time.time()
    ans = substring_divisible_pandigitals()
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
