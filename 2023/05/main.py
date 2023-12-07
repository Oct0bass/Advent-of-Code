import os
import itertools


class RangeMap:
    def __init__(self, maps: [(int, int, int)]):
        self.maps = sorted(maps, key=lambda m: m[1])

    def __getitem__(self, item: int | slice | range):
        if isinstance(item, slice) or isinstance(item, range):
            result: [range] = []
            if item.start < self.maps[0][1]:
                result += range(item.start, self.maps[0][1])
            for i in range(len(self.maps)):
                m = self.maps[i]
                #if m[1] <= item.start < m[1] + m[2]:

        else:
            for m in self.maps:
                if m[1] <= item < m[1] + m[2]:
                    return m[0] + (item - m[1])
            return item

    @staticmethod
    def read(text: str):
        lines = text.split("\n")
        if not lines[0][0].isdigit():
            del lines[0]
        return RangeMap([list(map(int, line.split())) for line in lines if line])


with open(os.getenv("input_file", "input.txt")) as file:
    sections = file.read().split("\n\n")

init_seeds = list(map(int, sections[0][7:].split()))

soil = RangeMap.read(sections[1])
fertilizer = RangeMap.read(sections[2])
water = RangeMap.read(sections[3])
light = RangeMap.read(sections[4])
temperature = RangeMap.read(sections[5])
humidity = RangeMap.read(sections[6])
location = RangeMap.read(sections[7])

final_locations = [location[humidity[temperature[light[water[fertilizer[soil[seed]]]]]]] for seed in init_seeds]

print(min(final_locations))

seed_range_generator = (range(init_seeds[i], init_seeds[i] + init_seeds[i + 1]) for i in range(0, len(init_seeds), 2))
seed_ranges = itertools.chain.from_iterable(seed_range_generator)

current_min = 2**31 - 1
for seed in seed_ranges:
    current_loc = location[humidity[temperature[light[water[fertilizer[soil[seed]]]]]]]
    if current_loc < current_min:
        current_min = current_loc

print(current_min)
