import time


def poker_wins(hands):
    """Input: A list of hands held by two players.
       Output: The number of wins by each player."""
    return hands[0]

def main():

    hands = open("poker.txt").read().splitlines()
    
    t0 = time.time()
    ans = poker_wins(hands)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
