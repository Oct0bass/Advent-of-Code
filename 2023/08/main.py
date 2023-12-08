import itertools
import math


key = {}
with open("input.txt") as f:
    directions = list(map(lambda c: c == "R", f.readline()[:-1]))
    for line in filter(lambda l: len(l) - 1, f.readlines()):
        k, v = line.split("=")
        key[k.strip()] = v.strip("() \n").split(", ")

steps = 0
location = "AAA"
for direction in itertools.cycle(directions):
    location = key[location][direction]
    steps += 1
    if location == "ZZZ":
        break

print(steps)


locations = set(filter(lambda k: k[-1] == "A", key.keys()))

# Idiotic brute force method (good luck running this)

# steps2 = 0
# for direction in itertools.cycle(directions):
#     new_locs = set()
#     for loc in locations:
#         new_locs.add(key[loc][direction])
#     locations = new_locs
#     steps2 += 1
#     if all(l[-1] == "Z" for l in locations):
#         break
#
# print(steps2)

def pathlen(start):
    result = 0
    location = start
    for direction in itertools.cycle(directions):
        location = key[location][direction]
        result += 1
        if location[-1] == "Z":
            return result


print(math.lcm(*(pathlen(l) for l in locations)))
