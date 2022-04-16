with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = [line.strip().split(' ') for line in inputs]

horiz = 0
depth = 0

for instruction in sanitized_inputs:
    if instruction[0] == "forward":
        horiz += int(instruction[1])
    if instruction[0] == "up":
        depth -= int(instruction[1])
    if instruction[0] == "down":
        depth += int(instruction[1])

print(horiz * depth)
