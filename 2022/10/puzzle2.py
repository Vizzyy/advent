with open('input.txt', 'r') as file:
    inputs = file.read()
instructions = [instruction.split(' ') for instruction in inputs.strip().split('\n')]
print(len(instructions))

cycle = 1
X = 1
cycle_values = {}
screen = [[' ' for x in range(40)] for y in range(6)]

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
    value = cycle_values[cycle]
    sprite_indexes = [value]
    if value % 40 > 0:
        sprite_indexes.append(value - 1)
    if value % 40 != 0:
        sprite_indexes.append(value + 1)
    sprite_indexes.sort()

    x_pos = (cycle % 40) - 1 if cycle % 40 != 0 else 39
    y_pos = cycle // 40 if cycle % 40 != 0 else (cycle // 40) - 1

    crt_indexes = [x_pos]

    print(f'{cycle} : {[y_pos, x_pos]} = {value}, crt_indexes: {crt_indexes}, sprite_indexes: {sprite_indexes}')
    overlapping = list(set(sprite_indexes) & set(crt_indexes))
    if len(overlapping) > 0:
        print(f'overlapping: {overlapping}')
    for index in overlapping:
        screen[y_pos][index] = '#'

[print(''.join(row)) for row in screen]
