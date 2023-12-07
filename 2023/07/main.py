import functools
import collections


def card_rank(c: str, joker=False):
    if c.isdigit():
        return int(c)
    else:
        if joker:
            if c == "J":
                return 1
            else:
                return ["T", "Q", "K", "A"].index(c) + 10
        else:
            return ["T", "J", "Q", "K", "A"].index(c) + 10


def type_rank(hand: str, joker=False):
    counts = collections.defaultdict(int)
    for c in hand:
        counts[c] += 1

    if joker:
        njokers = counts["J"]
        counts["J"] = 0
        counts[max(counts, key=counts.get)] += njokers

    c_items = sorted(counts.values(), reverse=True)
    max_category = c_items[0]
    if max_category >= 4:
        return max_category + 2
    elif max_category == 3:
        if c_items[1] >= 2:
            return 5
        else:
            return 4
    elif max_category == 2:
        if c_items[1] >= 2:
            return 3
        else:
            return 2
    else:
        return 1


def compare_decks(lhs, rhs, joker=False):
    if type_rank(lhs, joker=joker) == type_rank(rhs, joker=joker):
        for lcard, rcard in zip(lhs, rhs):
            lrank = card_rank(lcard, joker=joker)
            rrank = card_rank(rcard, joker=joker)
            if lrank != rrank:
                return lrank - rrank
    else:
        return type_rank(lhs, joker=joker) - type_rank(rhs, joker=joker)


with open("input.txt") as f:
    decks = [(line[:5], int(line[6:])) for line in f.readlines()]

sorted_decks = sorted(decks, key=functools.cmp_to_key(lambda lhs, rhs: compare_decks(lhs[0], rhs[0])))

total = 0
for (i, deck) in enumerate(sorted_decks):
    total += deck[1] * (i + 1)

print(total)

joker_sorted = sorted(decks, key=functools.cmp_to_key(lambda lhs, rhs: compare_decks(lhs[0], rhs[0], joker=True)))

joker_total = 0
for (i, deck) in enumerate(joker_sorted):
    joker_total += deck[1] * (i + 1)

print(joker_total)
