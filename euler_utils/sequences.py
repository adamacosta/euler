import numpy as np

# Utilities for generating sequences of numbers

def berggren(seeds):
    """Input: A list of Pythagorean triples.
       Output: Three children Pythagorean triples generated according to
       Berggren's three matrices."""
    A = np.array([[-1,2,2],
                  [-2,1,2],
                  [-2,2,3]])

    B = np.array([[1,2,2],
                  [2,1,2],
                  [2,2,3]])

    C = np.array([[1,-2,2],
                  [2,-1,2],
                  [2,-2,3]])
    result = []
    for b in seeds:
        result.extend([list(np.dot(A,b)),list(np.dot(B,b)),list(np.dot(C,b))])
    return result

def primitive_pythagorean_triples(n):
    """Input: A natural number n.
       Output: All primitive Pythagoren triples with sums <= n."""
    result = [[3,4,5]]
    for i in range(ceil(log(n))):
        result.extend(berggren(result))
    return [i for i in result if sum(i) <= n]

def pythagorean_triples(n):
    """Input: A natural number n.
       Output: All Pythagorean triples with sums <= n."""
    triples = primitive_pythagorean_triples(n)
    for prim in triples:
        if sum(prim) < n:
            i = 2
            while True:
                not_prim = list(i * np.array(prim))
                if sum(not_prim) < n:
                    triples.append(not_prim)
                    i += 1
                else:
                    break
    return [sorted(list(i)) for i in set(tuple(i) for i in triples)]

def triangle_numbers(n):
    """Input: A natural number n.
       Output: All triangle numbers up to n(n + 1)/2."""
    return list(np.arange(1, n + 1) * np.arange(2, n + 2) // 2)

def pentagon_numbers(n):
    """Input: A natural number n.
       Output: All pentagon numbers up to n(3n - 1)/2."""
    return list(np.arange(1, n + 1) * (3 * np.arange(1, n + 1) - 1) // 2)

def hexagon_numbers(n):
    """Input: A natural number n.
       Output: All hexagon numbers up to n(2n - 1)."""
    return list(np.arange(1, n + 1) * (2 * np.arange(1, n + 1) - 1))

def squarefree(n):
    """Input: A natural number n.
       Output: Squarefree numbers up to n."""
    return np.setdiff1d(np.arange(1, n), np.arange(1, floor(sqrt(n))) ** 2)

def main():

    # Add test code

    assert(triangle_numbers(13) == [1,3,6,10,15,21,28,36,45,55,66,78,91])

if __name__ == '__main__':
    main()
