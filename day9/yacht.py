# Score categories
# Change the values as you see fit
YACHT = lambda x : 50 if len(set(x)) == 1 else 0
ONES = lambda x : x.count(1)
TWOS = lambda x : x.count(2) * 2
THREES = lambda x : x.count(3) * 3
FOURS = lambda x : x.count(4) * 4
FIVES = lambda x : x.count(5) * 5
SIXES = lambda x : x.count(6) * 6
FULL_HOUSE = lambda x : sum(x) if len(set(x)) == 2 and ( 2 <= x.count(set(x).pop()) < 4) else 0
FOUR_OF_A_KIND = lambda x : fourOfAKind(x)
LITTLE_STRAIGHT = lambda x : 30 if len(set(x)) == 5 and (6 not in x) else 0
BIG_STRAIGHT = lambda x : 30 if len(set(x)) == 5 and (1 not in x) else 0
CHOICE = lambda x : sum(x)

def fourOfAKind(dice):
	fourOccurrences = -1

	for y in dice:
		if dice.count(y) >= 4:
			fourOccurrences = y
			break

	if fourOccurrences != -1:
		return fourOccurrences * 4

	return 0


def score(dice, category):
   	return category(dice)
