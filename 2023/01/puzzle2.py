import regex as re

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def convert_spelled_num(num):
    result = number_map[num]
    # print(f'{num} => {result}')
    return result


# [print(line) for line in inputs]

calibrations = 0
pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
pattern = re.compile(pattern)
# pattern.match(string)

for line in inputs:
    split = re.findall(pattern, line, overlapped=True) 
    split = [item for item in split if item != '']
    # print(split)
    first = None
    last = None
    for part in split:
        # print(part)
        if first is None and pattern.match(part):
            first = part
            last = part
        elif pattern.match(part):
            last = part
    if first in number_map.keys():
        first = convert_spelled_num(first)
    if last in number_map.keys():
        last = convert_spelled_num(last)
    result = int(f'{first}{last}')
    print(line, split, result)
    calibrations += result

print(calibrations)