with open('input.txt', 'r') as file:
    puzzle_input = file.read().strip().split('\n')


# [print(line) for line in puzzle_input]
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

digit_lengths = [len(display_key[int(key)]) for key in display_key.keys()]
print(digit_lengths)
[print(line) for line in puzzle_input]

unique_number_segment_lengths = [2, 4, 3, 7]

num_uniques_in_output = 0

for line in puzzle_input:
    segments = line[0]
    output = line[1]
    for segment in output:
        if len(segment) in unique_number_segment_lengths:
            num_uniques_in_output += 1

print(num_uniques_in_output)
