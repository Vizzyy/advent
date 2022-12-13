with open('input.txt', 'r') as file:
    inputs = file.read()
instructions = [instruction.split(' ') for instruction in inputs.strip().split('\n')]
print(len(instructions))

cycle = 1
X = 1
cycle_values = {}
target_cycles = [20, 60, 100, 140, 180, 220]

for idx in range(len(instructions)):
    instruction = instructions[idx]
    # print(f'{idx+1} - {instruction} - cycle: {cycle}')
    cycle_values[cycle] = X

    if instruction[0] == 'noop':
        cycle += 1

    elif instruction[0] == 'addx':
        cycle += 1
        cycle_values[cycle] = X
        X += int(instruction[1])
        cycle += 1
        cycle_values[cycle] = X

# print(cycle_values)

sum_signal = 0
for target in target_cycles:
    print(f'target: {target} = { cycle_values[target] * target}')
    sum_signal += cycle_values[target] * target

print(sum_signal)
