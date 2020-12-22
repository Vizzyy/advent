import re

with open('./input.txt', 'r') as file:
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

map_of_memory_addresses = {}


def find_addresses(regex, curr_address, index, value):
    # print(f"curr_address: {curr_address}")
    if index == 36:
        map_of_memory_addresses[int(curr_address, 2)] = value
        # print(f"returning: {curr_address}")
        return
    else:
        # print(f"regex[index]: {regex[index]}")
        if regex[index] == "X":
            find_addresses(regex, curr_address + "1", index+1, value)
            find_addresses(regex, curr_address + "0", index+1, value)
        else:
            find_addresses(regex, curr_address + regex[index], index+1, value)


for input in sanitized_inputs:
    parsed_input = input.split("=")
    parsed_input = [out.strip() for out in parsed_input]
    if parsed_input[0] == "mask":
        mask = parsed_input[1]
        # print(f"mask: {mask}")
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

        print(f"address:        {address}")
        print(find_addresses(address, "", 0, int(parsed_input[1])))

# print(memory)

total = 0

mem_addresses_used = map_of_memory_addresses.keys()
for mem in mem_addresses_used:
    total += map_of_memory_addresses[mem]

print(total)
