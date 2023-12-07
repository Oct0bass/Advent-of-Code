import math

def max_time(race_time, record):
    det = math.sqrt(race_time * race_time - 4 * record)
    return math.ceil((race_time + det)/2 - 1) - math.floor((race_time - det)/2 + 1) + 1

with open("input.txt") as f:
    durations_strings = f.readline().split()[1:]
    records_strings = f.readline().split()[1:]

durations = list(map(int, durations_strings))
records = list(map(int, records_strings))

product = 1
for (duration, record) in zip(durations, records):
    product *= max_time(duration, record)

print(product)

one_duration = int("".join(durations_strings))
one_record = int("".join(records_strings))
print(max_time(one_duration, one_record))