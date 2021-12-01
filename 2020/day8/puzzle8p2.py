with open('input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "").replace("+", "").split(" ")
    sanitized_inputs.append(temp)

# print(sanitized_inputs)
# print(len(sanitized_inputs))

nops_or_jmps = []
for i in range(len(sanitized_inputs)):
    instruction = sanitized_inputs[i]
    if instruction[0] == "jmp" or instruction[0] == "nop":
        nops_or_jmps.append(i)

# print(f"nop/jmp options: {len(nops_or_jmps)}")
# print(nops_or_jmps)

outer_check = False
outer_accum = 0
for index in nops_or_jmps:
    sanitized_inputs = []

    for num in inputs:
        temp = num.replace("\n", "").replace("+", "").split(" ")
        sanitized_inputs.append(temp)
    option = sanitized_inputs[index]

    if option[0] == "jmp":
        sanitized_inputs[index] = ["nop", option[1]]
    else:
        sanitized_inputs[index] = ["jmp", option[1]]

    repeat_check_array = [0 for x in range(len(sanitized_inputs))]

    accumulator = 0
    pointer = 0
    while True:
        if pointer >= len(sanitized_inputs):
            print(f"before: {option} - after: {sanitized_inputs[index]} - {index}")
            print(f"successfully terminated {pointer} -- accum: {accumulator}")
            outer_check = True
            outer_accum = accumulator
            break
        if repeat_check_array[pointer] > 0:
            # print("infinite loop")
            break
        repeat_check_array[pointer] += 1

        instruction = sanitized_inputs[pointer]

        if instruction[0] == "acc":
            accumulator += int(instruction[1])
            pointer += 1
        if instruction[0] == "jmp":
            pointer += int(instruction[1])
        if instruction[0] == "nop":
            pointer += 1

    if outer_check:
        break

print(f"outer_accum {outer_accum}")
