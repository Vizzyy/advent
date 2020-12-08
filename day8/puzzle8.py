with open('./input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "").replace("+", "").split(" ")
    sanitized_inputs.append(temp)

# print(sanitized_inputs)
# print(len(sanitized_inputs))
#
repeat_check_array = [0 for x in range(len(sanitized_inputs))]
# print (repeat_check_array)

accumulator = 0
pointer = 0
while True:
    if repeat_check_array[pointer] > 0:
        break
    repeat_check_array[pointer] += 1
    instruction = sanitized_inputs[pointer]

    if instruction[0] == "acc":
        accumulator += int(instruction[1])
        pointer += 1
    elif instruction[0] == "jmp":
        pointer += int(instruction[1])
    elif instruction[0] == "nop":
        pointer += 1

print(accumulator)