with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n\n')

inputs2 = [[int(num) for num in inp.split('\n')] for inp in inputs]

highest = 0
for elf in inputs2:
    temp = sum(elf)
    if temp > highest:
        highest = temp

print(highest)
