with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = [line.strip() for line in inputs]
original_inputs = sanitized_inputs


def get_most_common_at_idx(input_list, idx):
    count = 0
    for line in input_list:
        if int(line[idx]) == 1:
            count += 1
        else:
            count -= 1

    if count >= 0:
        return 1
    else:
        return 0


ptr = 0
while len(sanitized_inputs) != 1:
    temp_input = []
    most_common_at_idx = get_most_common_at_idx(sanitized_inputs, ptr)
    print(f"most_common_at_idx: {most_common_at_idx}")
    for line_idx in range(len(sanitized_inputs)):
        line = sanitized_inputs[line_idx]
        if int(line[ptr]) == most_common_at_idx:
            temp_input.append(line)
    sanitized_inputs = temp_input
    ptr += 1

print(sanitized_inputs)
oxy = sanitized_inputs
sanitized_inputs = original_inputs

ptr = 0
while len(sanitized_inputs) != 1:
    temp_input = []
    most_common_at_idx = get_most_common_at_idx(sanitized_inputs, ptr)
    if most_common_at_idx == 1:
        most_common_at_idx = 0
    else:
        most_common_at_idx = 1
    print(f"least_common_at_idx: {most_common_at_idx}")
    for line_idx in range(len(sanitized_inputs)):
        line = sanitized_inputs[line_idx]
        if int(line[ptr]) == most_common_at_idx:
            temp_input.append(line)
    sanitized_inputs = temp_input
    ptr += 1

print(sanitized_inputs)
co2 = sanitized_inputs

print(int(f"{oxy[0]}", 2) * int(f"{co2[0]}", 2))
