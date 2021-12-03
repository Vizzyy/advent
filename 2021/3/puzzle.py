with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = [line.strip() for line in inputs]

bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in sanitized_inputs:
    for idx in range(len(line)):
        if int(line[idx]) == 0:
            bits[idx] -= 1
        else:
            bits[idx] += 1

epsilon = ""
gamma = ""

for idx in bits:
    if idx > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))

