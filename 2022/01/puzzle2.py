with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n\n')

inputs2 = [[int(num) for num in inp.split('\n')] for inp in inputs]

sums = []
for elf in inputs2:
    temp = sum(elf)
    sums.append(temp)

sums.sort()

print(sum(sums[-3:]))
