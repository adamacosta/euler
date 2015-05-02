import time

def coin_sums(coins, total):
    """Input: A list of coin values and a target total.
    Output: The number of ways in which total can be made from
    any number of any coins."""
    possibles = [1] + [0 for i in range(total)]
    for i in range(len(coins)):
        for j in range(coins[i], total + 1):
            possibles[j] += possibles[j - coins[i]]
    return possibles.pop()

coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200

t0 = time.time()
ans = coin_sums(coins, total)
t1 = time.time()
elapsed = t1 - t0

print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")
