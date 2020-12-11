from copy import copy
import time

with open('./input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(int(temp))

sanitized_inputs.sort()
print(sanitized_inputs)
print(len(sanitized_inputs))

#  Part Two

# Since the last translation is always +3 we can omit it
# However you can skip initial adaptors going from 0 -> 3
adaptors = [0] + sanitized_inputs
print(adaptors)
print(len(adaptors))
print()
solutions = []


cache = [None for x in range(len(adaptors))]

#[0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]


def possible_combinations(start_index: int):

    combo_count = 0
    partial_adaptor_list = adaptors[start_index:]
    start_num = partial_adaptor_list[0]

    possible_next_choices = []
    for adaptor in partial_adaptor_list:
        if start_num < adaptor <= start_num + 3:
            # combo_count += 1
            possible_next_choices.append(adaptor)

    if not possible_next_choices:
        combo_count = 1
    else:
        for possibility in possible_next_choices:
            cached_value = cache[adaptors.index(possibility)]
            print(f"cache index {possibility} = {cached_value}")
            if cached_value is not None:
                combo_count += cached_value

    print(start_index, start_num, partial_adaptor_list, combo_count)
    print()
    cache[start_index] = combo_count
    return combo_count


for i in range(len(adaptors) - 1, -1, -1):
    possible_combinations(i)

# print(cache)

print(cache)