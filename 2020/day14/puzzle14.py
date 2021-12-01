with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
print(sanitized_inputs)

memory = [0 for mem in range(99999)]
print(f"memory size: {len(memory)}")
mask = ""
false_mask = ""  # to mask 0 -- true AND false equals false
true_mask = ""  # to mask 1 -- true OR false equals true

for input in sanitized_inputs:
    parsed_input = input.split("=")
    parsed_input = [out.strip() for out in parsed_input]
    if parsed_input[0] == "mask":
        mask = parsed_input[1]
        false_mask = "".join(["1" if bit == "X" or bit == "1" else "0" for bit in mask])
        true_mask = "".join(["0" if bit == "X" or bit == "0" else "1" for bit in mask])
        print(f"mask = {mask}, false_mask = {false_mask}, true_mask = {true_mask}")
    else:
        mem_pos = int(parsed_input[0].replace('mem[', '').replace(']', ''))

        unmasked_int = int(parsed_input[1])
        binary_val = f'{int(unmasked_int):036b}'
        false_mask_int = int(str(false_mask), 2)
        true_mask_int = int(str(true_mask), 2)
        print(f"val: {unmasked_int}, binary_val: {binary_val}")
        masked_output = unmasked_int & false_mask_int
        masked_output = masked_output | true_mask_int
        masked_output_binary = f'{int(masked_output):036b}'
        print(f"masked_val: {masked_output_binary}")

        memory[mem_pos] = masked_output


# print(memory)

total = 0

for mem in memory:
    total += mem

print(total)
