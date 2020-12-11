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

jolt_differences = [0 for x in range(4)]
jolt_differences[1] += 1  # 0 -> 1 difference from outlet not in data-set
jolt_3_diff_indexes = []
for i in range(len(sanitized_inputs)):
    try:
        diff = sanitized_inputs[i + 1] - sanitized_inputs[i]
        jolt_differences[diff] += 1
        if diff == 3:
            jolt_3_diff_indexes.append(i)
    except:
        jolt_differences[3] += 1

print(jolt_differences)
print(jolt_differences[1] * jolt_differences[3])
print(jolt_3_diff_indexes)
print()

#  Part Two

# Since the last translation is always +3 we can omit it
# However you can skip initial adaptors going from 0 -> 3
# adaptors = [0] + sanitized_inputs
adaptors = [46, 47, 48, 49]
print(adaptors)
print(len(adaptors))

solutions = []


def possible_combinations(start_index, path):
    combo_count = 0
    partial_adaptor_list = adaptors[start_index:]
    # print(f"adaptor {adaptors[start_index]} - partial list: {partial_adaptor_list} - path so far {path}")
    possible_next_choices = []
    start_num = partial_adaptor_list[0]
    for adaptor in partial_adaptor_list:
        if start_num < adaptor <= start_num + 3:
            possible_next_choices.append(adaptor)
            combo_count += 1

    # print(f"possible next steps: {possible_next_choices}")
    for possibility in possible_next_choices:
        new_path = copy(path)
        # print(f"new path: {new_path}")
        new_path.append(possibility)
        # print(f"new path: {new_path}")
        combo_count += possible_combinations(adaptors.index(possibility), new_path)

    if not possible_next_choices:
        solution = copy(path)
        # print(solution)
        solutions.append(solution)

    # print(f"adaptor {adaptors[start_index]} - count {combo_count}")
    return combo_count


start_time = time.time()
print(start_time)
possible_combinations(0, [adaptors[0]])
print("--- %s seconds ---" % (time.time() - start_time))
print("Solutions:")
print(len(solutions))
print("--- %s seconds ---" % (time.time() - start_time))
