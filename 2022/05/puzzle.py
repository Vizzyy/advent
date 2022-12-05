stack_max = 9

with open('input.txt', 'r') as file:
    inputs = file.read()
xs, instructions = inputs.split('\n\n')
xs = xs.split('\n')[:-1]
[print(x) for x in xs]
print()
grid = []
for x in xs:
    tenp = [x[i:i+4].strip() for i in range(0, len(x), 4)]
    print(f'tenp: {tenp}')
    # temp = x.replace('   ', '').split(' ')
    # print(temp)
    grid.append(tenp)

# [print(vert) for vert in grid]
print()

padded_grid = []
for row in grid:
    new_row = row
    if len(row) != stack_max:
        new_row = new_row + ([''] * (stack_max - len(row)))
    # print(new_row)
    padded_grid.append(new_row)


[print(row) for row in padded_grid]

print()
padded_grid = padded_grid[::-1]
if len(padded_grid) != stack_max:
    print("adding row")
    padded_grid.append([''] * stack_max)
[print(row) for row in padded_grid]

# traverse a matrix and swap
# mat[i][j] with mat[j][i]
for i in range(stack_max):
    for j in range(i + 1):
        t = padded_grid[i][j]
        padded_grid[i][j] = padded_grid[j][i]
        padded_grid[j][i] = t

print()
[print(row) for row in padded_grid]

# reduce grid again
reduced_grid = []
for row in padded_grid:
    new_row = []
    for item in row:
        if item != "":
            new_row.append(item)
    reduced_grid.append(new_row)

print()
[print(row) for row in reduced_grid]

print()
instructions = instructions.strip().split('\n')

print(instructions)
for instruction in instructions:
    move_num, direction = instruction.split(' from ')
    move_num = int(move_num.split('move ')[1])
    direction = [int(dr) for dr in direction.split(' to ')]
    print(move_num, direction)

    while move_num > 0:
        popped = reduced_grid[direction[0]-1].pop()
        print(f'popped: "{popped}"')
        if popped == "":
            continue
        reduced_grid[direction[1]-1].append(popped)
        move_num -= 1

print()
[print(row) for row in reduced_grid]


