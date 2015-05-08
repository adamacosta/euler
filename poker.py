# General helper functions

def is_same(lc):
    """Input: A list of characters.
       Output: Whether they are all the same character."""
    return sum([lc[i]==lc[i+1] for i in range(len(lc) - 1)]) == len(lc) - 1

def is_consecutive(ln):
    """Input: A list of numbers.
       Output: Whether they are consecutive when sorted."""
    sln = sorted(ln)
    return sum([sln[i]+1==sln[i+1] for i in range(len(sln) - 1)]) == len(sln) - 1

# Private dictionaries containing card/hand to score mappings

_card_vals = {'2C':1, '2H':1, '2S':1, '2D':1,
             '3C':2, '3H':2, '3S':2, '3D':2,
             '4C':3, '4H':3, '4S':3, '4D':3,
             '5C':4, '5H':4, '5S':4, '5D':4,
             '6C':5, '6H':5, '6S':5, '6D':5,
             '7C':6, '7H':6, '7S':6, '7D':6,
             '8C':7, '8H':7, '8S':7, '8D':7,
             '9C':8, '9H':8, '9S':8, '9D':8,
             'TC':9, 'TH':9, 'TS':9, 'TD':9,
             'JC':10, 'JH':10, 'JS':10, 'JD':10,
             'QC':11, 'QH':11, 'QS':11, 'QD':11,
             'KC':12, 'KH':12, 'KS':12, 'KD':12,
             'AC':13, 'AH':13, 'AS':13, 'AD':13}

_hand_scores = {'royal_flush':10, 'straight_flush':9, 'four_kind':8,
                'full_house':7, 'flush':6, 'straight':5, 'three_kind':4,
                'two_pair':3, 'one_pair':2, 'high_card':1}

# Parsing functions to create scorable hands and cards from input lines

def make_hands(line):
    """Input: A line of ten cards.
       Output: A list of two lists, each containing the cards
               of each player."""
    cards = line.split(' ')
    hands = [[],[]]
    for i in range(5):
        hands[0].append(cards[i])
    for i in range(5, 10):
        hands[1].append(cards[i])
    return hands

def parse_card(card):
    """Input: A poker card such as AC.
       Output: A <face, suit> pair."""
    result = {}
    result['face'] = _card_vals[card]
    result['suit'] = card[1]
    return result

# Functions to parse hands into outcomes (pair, flush, etc)

def high_card(hand):
    """Input: A poker hand.
       Output: The sum of face values in the hand."""
    return 10 * max([parse_card(card)['face'] for card in hand]) + sum([parse_card(card)['face'] for card in hand])

def pair(hand):
    """Input: A poker hand.
       Output: A list of face values of any pairs found."""
    result = []
    for i in range(5):
        val = parse_card(hand[i])['face']
        for j in range(i + 1, 5):
            if parse_card(hand[j])['face'] == val:
                result.append(val)
    return result

def three(hand):
    """Input: A poker hand.
       Output: The face value of any three of a kind."""
    for i in range(5):
        val = parse_card(hand[i])['face']
        for j in range(i + 1, 5):
            if parse_card(hand[j])['face'] == val:
                for k in range(j + 1, 5):
                    if parse_card(hand[k])['face'] == val:
                        return val
    return 0

def four(hand):
    """Input: A poker hand.
       Output: The face value of any four of a kind."""
    for i in range(5):
        val = parse_card(hand[i])['face']
        for j in range(i + 1, 5):
            if parse_card(hand[j])['face'] == val:
                for k in range(j + 1, 5):
                    if parse_card(hand[k])['face'] == val:
                        for l in range(k + 1, 5):
                            if parse_card(hand[l])['face'] ==  val:
                                return val
    return 0

def full_house(hand):
    """Input: A poker hand.
       Output: The face value of the high card in a full house."""
    if len(pair(hand)) == 0: return 0
    return three(hand)

def is_flush(hand):
    """Input: A poker hand.
       Output: Whether or not the hand is a flush."""
    return is_same([parse_card(card)['suit'] for card in hand])

def is_straight(hand):
    """Input: A poker hand.
       Output: Whether or not the hand is a straight."""
    return is_consecutive([parse_card(card)['face'] for card in hand])

# Generates numerical scores from poker hands

def score(hand):
    """Input: A poker hand.
       Output: The score of the hand."""
    result = 0
    if is_straight(hand):
        if is_flush(hand):
            return high_card(hand) + 10000 * _hand_scores['straight_flush']
        return high_card(hand) + 10000 * _hand_scores['straight']
    if is_flush(hand):
        return high_card(hand) + 10000 * _hand_scores['flush']
    if four(hand):
        return high_card(hand) + 1000 * four(hand) + 10000 * _hand_scores['four_kind']
    if full_house(hand):
        return max(pair(hand)) + 1000 * full_house(hand) + 10000 * _hand_scores['full_house']
    if three(hand):
        return high_card(hand) + 1000 * three(hand) + 10000 * _hand_scores['three_kind']
    if len(pair(hand)) == 2:
        return high_card(hand) + 1000 * max(pair(hand)) + 10000 * _hand_scores['two_pair']
    if len(pair(hand)) == 1:
        return high_card(hand) + 1000 * max(pair(hand)) + 10000 * _hand_scores['one_pair']
    return high_card(hand)

def winning_hand(hands):
    """Input: A pair of poker hands.
       Output: The index of the winner of the hand (0, 1)."""
    return int(score(hands[0]) < score(hands[1]))

def main():

    sample1 = 'AC KC QC JC TC KS QS JS TS 9S'
    hands = make_hands(sample1)
    print(hands)
    for hand in hands:
        print(score(hand))

    sample2 = '3C 4S 5S 6D 7S 7C 8C TC JC QC'
    hands = make_hands(sample2)
    print(hands)
    for hand in hands:
        print(score(hand))

    sample3 = 'KD KS 9S 7C 2S KS KD QS 4H JC'
    hands = make_hands(sample3)
    print(hands)
    for hand in hands:
        print(score(hand))

    sample4 = 'AH 9S 4D 9D 8S 4H JS 3C TC 8D'
    hands = make_hands(sample4)
    print(hands)
    for hand in hands:
        print(score(hand))

if __name__ == '__main__':
    main()
