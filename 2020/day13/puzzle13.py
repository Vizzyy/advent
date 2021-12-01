from copy import copy

with open('input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
# print(sanitized_inputs)
# print()

timestamp_start = int(sanitized_inputs[0])
options = sanitized_inputs[1].split(',')
options_parsed = [int(x) for x in options if x != "x"]
options_parsed.sort()
print(timestamp_start)
print(options_parsed)

timestamp_mod = copy(timestamp_start)
result = None
while not result:

    for option in options_parsed:
        if timestamp_mod % option == 0:
            result = option
            break

    if not result:
        timestamp_mod += 1


print(result)
print(f"time end: {timestamp_mod}")
print(result * (timestamp_mod - timestamp_start))
