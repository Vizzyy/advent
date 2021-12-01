with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = [int(line.strip()) for line in inputs]

previous = sanitized_inputs[0]
num_increased = 0

for value in sanitized_inputs[1:]:
    if value > previous:
        num_increased += 1
    previous = value

print(num_increased)
