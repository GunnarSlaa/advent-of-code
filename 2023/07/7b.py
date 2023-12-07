with open("input", "r") as file:
    lines = file.read().strip().split("\n")

hands = [line.split() for line in lines]
values = {"A": 14,
          "K": 13,
          "Q": 12,
          "J": 1,
          "T": 10, }


class Hand(object):

    def __init__(self, hand):
        self.hand_type = hand_type(hand[0])
        self.hand = [int(c) if c.isdigit() else values[c] for c in hand[0]]
        self.bet = int(hand[1])

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for i in range(len(self.hand)):
            if self.hand[i] != other.hand[i]:
                return self.hand[i] < other.hand[i]


def hand_type(hand):
    check_hand = hand.replace("J", "")
    if len(check_hand) == 0:
        max_same = 5
    else:
        max_same = max([hand.count(c) for c in check_hand]) + hand.count("J")
    if max_same == 5:
        return 6
    elif max_same == 4:
        return 5
    elif max_same == 3:
        if len(set(check_hand)) == 2:
            return 4
        else:
            return 3
    elif max_same == 2:
        if len(set(check_hand)) == 3:
            return 2
        else:
            return 1
    else:
        return 0


hands = [Hand(hand) for hand in hands]
hands.sort()
total = 0
for i, hand in enumerate(hands):
    total += (i + 1) * hand.bet
print(total)
