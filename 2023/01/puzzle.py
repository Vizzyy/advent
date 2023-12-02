with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

# print(inputs)
# [print(line) for line in inputs]

calibrations = []

for line in inputs:
    first = None
    last = None
    for letter in line:
        if first is None and letter.isnumeric():
            first = letter
            last = letter
        elif letter.isnumeric():
            last = letter
    calibrations.append(int(f'{first}{last}'))

# print(calibrations)
total = sum(calibrations)
print(total)