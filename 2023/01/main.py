with open("example.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    numbers = list(filter(str.isdigit, line))
    if len(numbers) > 0:
        total += int(numbers[0] + numbers[-1])

print(total)

digit_names = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

ltotal = 0
for line in lines:
    first=0
    last=0
    for i in range(len(line)):
        if first and last:
            break
        start = line[:i]
        end = line[i:]
        if start and not first:
            if start[-1].isdigit():
                first = int(start[-1])
            else:
                for name in digit_names:
                    if start.endswith(name):
                        first = digit_names.index(name) + 1
                        break
        if end and not last:
            if end[-1].isdigit():
                last = int(end[-1])
            else:
                for name in digit_names:
                    if end.startswith(name):
                        last = digit_names.index(name) + 1
                        break

    ltotal += first * 10 + last



print(ltotal)
