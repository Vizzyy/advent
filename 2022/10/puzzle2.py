with open('test.txt', 'r') as file:
    inputs = file.read()
instructions = [instruction.split(' ') for instruction in inputs.strip().split('\n')]
print(len(instructions))

cycle = 1
X = 1
cycle_values = {}
screen = [['.' for x in range(40)] for y in range(6)]

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

print(cycle_values)
print()

for cycle in sorted(list(cycle_values.keys())):
    x_pos = (cycle % 40) - 1 if cycle % 40 != 0 else 39
    y_pos = cycle // 40 if cycle % 40 != 0 else (cycle // 40) - 1
    value = cycle_values[cycle]
    # screen[y_pos][x_pos] = f'{value}'
    # print(f'{cycle} : {[y_pos, x_pos]} = {value}')
    try:
        if x_pos > 0:
            screen[y_pos][x_pos - 1] = '#' if value == cycle else '.'
        screen[y_pos][x_pos] = '#' if value == cycle else '.'
        if x_pos < 39:
            screen[y_pos][x_pos + 1] = '#' if value == cycle else '.'
    except:
        pass

[print(row) for row in screen]
