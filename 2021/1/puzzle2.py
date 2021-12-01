with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = [int(line.strip()) for line in inputs]

sets = []
num_increased = 0

for i in range(len(sanitized_inputs)):
    if (i + 2) < len(sanitized_inputs):
        sets.append([sanitized_inputs[i], sanitized_inputs[i + 1], sanitized_inputs[i + 2]])

previous = sum(sets[0])
for s in sets[1:]:
    if sum(s) > previous:
        num_increased += 1
    previous = sum(s)

print(num_increased)
