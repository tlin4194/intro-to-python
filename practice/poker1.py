"""
Poker Hands
Background: This problem involves 5-card hands in the game of poker, represented as strings. Hands are represented by 5 cards separated by spaces, with each card composed of two characters, the first for its rank and the second for its suit. 
There are 13 ranks. We use "T", "J", "Q", "K", and "A" to represent the ranks Ten, Jack, Queen, King, and Ace, and the characters "2"-"9" for ranks 2-9. 
There are four suits: Clubs, Diamonds, Hearts, and Spades. The first letter of each suit is used to represent the suit. 
For example, "JD JS TH 2D 5C" is a hand with a Jack of Diamonds, a Jack of Spades, a Ten of Hearts, a Two of Diamonds, and a Five of Clubs. 
You will write 4 functions that deal with these hands.

10 = 10
Jack = 11
Queen = 12
King = 13
Ace = 1

isValidHand
This function takes a string and returns True if it follows the above specification, and False otherwise. 
For example, if the hand does not have exactly 5 cards, if the cards are not separated by exactly one space, or if a rank or suit is not valid, return False.

isFlush
This function takes a string and returns True if it is a valid hand and all of its cards have the same suit.
It returns False otherwise.

isRoyalFlush
This function takes a string and returns True if the hand is a royal flush, and False otherwise.
A royal flush has three properties: it is a valid hand, all of its cards have the same suit, and there is exactly one of each of the following ranks: Ten, Jack, Queen, King, and Ace. These cards can be in any order.

hasPair
This function takes a string and returns True if it is a valid hand and that hand contains at least two cards of the same rank, and False otherwise.
Note that this does not correspond exactly to the Poker hand of "one pair", since hasPair(hand) will return True for a hand with three-of-a-kind.
For example, hasPair("KD KS 7H 8C KC") returns True.
"""

import random

ranks = "23456789TJQKA"
suits = "CDHS"

#  TEST CASES
invalid_hands = [
    ("AH", "AH", "7S", "4S", "6S"),  # Duplicate cards
    ("5S", "JC", "TD", "5D", "5D"),  # Duplicate cards
    ("AH", "1D", "7S", "4S", "6S"),  # Incorrect rank
    ("ZS", "JC", "TD", "5D", "4D"),  # Incorrect rank
    ("AH", "5D", "7S", "4X", "6S"),  # Incorrect suit
    ("5S", "JC", "TD", "5D", "4Z"),  # Incorrect suit
    ("AH5D", "7S", "4S", "6S"),  # Incorrect format (missing space)
    ("5SJC", "TD", "5D", "4D"),  # Incorrect format (missing space)
]
flushes = [
    ("2H", "5H", "7H", "9H", "KH"),  # Hearts Flush
    ("3C", "4C", "6C", "9C", "QC"),  # Clubs Flush
    ("4D", "5D", "8D", "JD", "KD"),  # Diamonds Flush
    ("2S", "6S", "8S", "QS", "KS"),  # Spades Flush
    ("5H", "7H", "8H", "QH", "AH"),  # Hearts Flush
]
royal_flushes = [
    ("TH", "JH", "QH", "KH", "AH"),  # Hearts Royal Flush
    ("TC", "JC", "QC", "KC", "AC"),  # Clubs Royal Flush
]
pairs = [
    ("2H", "2D", "5S", "9C", "KH"),  # Pair of Twos
    ("3S", "3H", "6C", "8D", "QC"),  # Pair of Threes
    ("4C", "4S", "4D", "JD", "KD"),  # Triple of Fours
]


def main():
    # Generate 6 hands
    deck = create_deck()
    valid_hands = [get_hand(deck) for _ in range(5)]

    print("Testing isValidHand")
    for h in valid_hands:
        print(f"{h=} {isValidHand(h)}")
    for h in invalid_hands:
        print(f"{h=} {isValidHand(h)}")

    print("Testing isFlush")
    for h in flushes:
        print(f"{h=} {isFlush(h)}")

    print("Testing isRoyalFlush")
    for h in royal_flushes:
        print(f"{h=} {isRoyalFlush(h)}")

    print("Testing hasPair")
    for h in pairs:
        print(f"{h=} {hasPair(h)}")


def create_deck():
    deck = set()
    for r in ranks:
        for s in suits:
            deck.add(r + s)
    return deck


def get_hand(deck):
    return tuple(random.sample(list(deck), 5))


def isValidHand(hand):
    if len(hand) != 5:
        return False

    seen = set()
    for card in hand:
        if len(card) != 2:
            return False
        # rank = card[0]
        # suit = card[1]
        # is the same thing as
        rank, suit = card[0], card[1]
        if rank not in ranks or suit not in suits:
            return False
        if card in seen:
            return False
        seen.add(card)
    return True


def isFlush(hand):
    # hand = ("2H", "5H", "7S", "9H", "KH")
    if not isValidHand(hand):
        return False
    for card in range(len(hand)):
        if hand[0][1] != hand[card][1]:
            return False
    return True


def isRoyalFlush(hand):
    # hand = ("2H", "5H", "7S", "9H", "KH")
    check_dupes = set()
    royal = "TJQKA"
    if not isFlush(hand):
        return False
    for card in range(len(hand)):
        if hand[card][0] not in royal:
            return False
        if hand[card][0] in check_dupes:
            return False
        check_dupes.add(hand[card][0])
    return True


def hasPair(hand):
    if not isValidHand(hand):
        return False
    # ("2H", "5D", "5S", "2C", "KH")
    ranks_seen = set()
    for i in range(len(hand)):
        # 0, 1, 2, 3, 4
        ranks_seen.add(hand[i][0])
        if hand[i][0] in ranks_seen:
            return True
    return False


main()
