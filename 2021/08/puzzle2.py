with open('input.txt', 'r') as file:
    puzzle_input = file.read().strip().split('\n')

puzzle_input = [[display.split(' ') for display in displays] for displays in [line.split(' | ') for line in puzzle_input]]

display_key = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

visual = """
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


def segment_exists_as_subset(subset, superset):
    for letter in subset:
        if letter in superset:
            continue
        else:
            return False
    return True


running_total = 0
for line in puzzle_input:

    print(line)
    segments = line[0]
    output = line[1]

    segments.sort(key=lambda s: len(s))

    segment_map = {
        1: segments[0],
        7: segments[1],
        4: segments[2],
        8: segments[9]
    }
    segments = segments[3:9]

    segment_values = [segment_map[key] for key in segment_map.keys()]

    while len(segment_map.keys()) != 10:
        for segment in segments:
            try:
                # if len is 5 then it is either a 2, 3, or 5
                if len(segment) == 5:
                    # if 7 fits into it, then it can only be a 3
                    if segment_exists_as_subset(segment_map[7], segment):
                        segment_map[3] = segment
                        del segment_values[segment_values.index(segment)]
                        continue
                    # if it fits into a 9, then it must be 5
                    if segment_exists_as_subset(segment, segment_map[9]):
                        segment_map[5] = segment
                        del segment_values[segment_values.index(segment)]
                        continue
                    # if the others are found, then it must be a 2
                    if 5 in segment_map.keys() and 3 in segment_map.keys():
                        segment_map[2] = segment
                        del segment_values[segment_values.index(segment)]
                        continue
                # else the len is 6 and it is a 0, 6, or 9
                elif len(segment) == 6:
                    # if 4 fits into it, then it can only be a 9
                    if segment_exists_as_subset(segment_map[4], segment):
                        segment_map[9] = segment
                        del segment_values[segment_values.index(segment)]
                        continue
                    # if 7 fits into it, then it can only be a 0
                    if segment_exists_as_subset(segment_map[7], segment):
                        segment_map[0] = segment
                        del segment_values[segment_values.index(segment)]
                        continue
                    # if the others are found, then it must be a 6
                    if 9 in segment_map.keys() and 0 in segment_map.keys():
                        segment_map[6] = segment
                        del segment_values[segment_values.index(segment)]
                        continue
            except Exception as e:
                # print(e)
                pass

            # repopulate values list
            segment_values = [segment_map[key] for key in segment_map.keys()]

    print(segment_map)
    segment_values_map = {}
    for key in segment_map:
        segment_values_map[''.join(sorted(segment_map[key]))] = key
    print(segment_values_map)

    converted_digit = ""
    for digit in output:
        sorted_digit = ''.join(sorted(digit))
        converted_digit += str(segment_values_map[sorted_digit])
    converted_digit = int(converted_digit)
    print(converted_digit)
    running_total += converted_digit

print()
print(running_total)
