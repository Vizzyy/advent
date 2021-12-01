import re

with open('test_input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
# print(sanitized_inputs)

memory = [0 for mem in range(100)]

memory_addresses_in_binary = [f'{int(mem):036b}' for mem in range(100)]
print("done with setup")
# print(memory_addresses_in_binary)
# print(f"memory size: {len(memory)}")
mask = ""
false_mask = ""  # to mask 0 -- true AND false equals false
true_mask = ""  # to mask 1 -- true OR false equals true

for input in sanitized_inputs:
    parsed_input = input.split("=")
    parsed_input = [out.strip() for out in parsed_input]
    if parsed_input[0] == "mask":
        mask = parsed_input[1]
        print(f"mask: {mask}")
    else:
        mem_pos = int(parsed_input[0].replace('mem[', '').replace(']', ''))
        mem_pos_binary = f'{int(mem_pos):036b}'
        # print(f"mem_pos_binary: {mem_pos_binary}")

        address = ""
        for i in range(len(mask) - 1, -1, -1):
            # print(f"mask[i]: {mask[i]}")
            if mask[i] == "0":
                address = mem_pos_binary[i] + address
            elif mask[i] == "1":
                # print(f"mem_pos_binary[i]: {mem_pos_binary[i]}")
                address = str(int(mask[i]) | int(mem_pos_binary[i])) + address
            else:
                address = "X" + address
            # print(f"address: {address}")

        # print(f"address:        {address}")

        address_regex = address.replace("X", ".")
        print(f"address_regex:  {address_regex}")
        for i in range(len(memory_addresses_in_binary)):
            x = re.match(address_regex, memory_addresses_in_binary[i])
            if x:
                print(f"x: {x}, i: {i}, memory_addresses_in_binary[i]: {memory_addresses_in_binary[i]}")
                memory[int(memory_addresses_in_binary[i], 2)] = int(parsed_input[1])

# print(memory)

total = 0

for mem in memory:
    total += mem

print(total)
