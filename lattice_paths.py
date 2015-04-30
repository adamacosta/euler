import time
import numpy as np

def find_paths(num):
    """Input: The size of a grid.
    Output: The number of paths from the upper left to
    lower right using only right and down moves."""
    dim = (num + 1) * (num + 1)
    adj = np.zeros(shape=(dim, dim), dtype=int)
    longest = 2 * num
    # Construct an adjacency matrix of a directed graph in
    # which each node has an edge to the right and down
    for i in range(dim - 1):
        adj[i][i + 1] = 1
    for i in range(dim - num - 1):
        adj[i][i + 1 + num] = 1
    mat = np.matrix(adj, copy=False)
    # Uses matrix exponentiation to find the number of paths
    # between all nodes of length longest
    return (mat ** longest).getA()[0][dim - 1]

num = 20

t0 = time.time()
ans = find_paths(num)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
