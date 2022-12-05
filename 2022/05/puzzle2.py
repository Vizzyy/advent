stack_max = 9

with open('input.txt', 'r') as file:
    inputs = file.read()
xs, instructions = inputs.split('\n\n')
xs = xs.split('\n')[:-1]
grid = []
for x in xs:
    # split up rows into chunks of 4 chars representing one column each
    tenp = [x[i:i+4].strip() for i in range(0, len(x), 4)]
    grid.append(tenp)

# pad the grid to get a proper matrix
padded_grid = []
for row in grid:
    new_row = row
    if len(row) != stack_max:
        new_row = new_row + ([''] * (stack_max - len(row)))
    padded_grid.append(new_row)

# reverse the order of the rows
padded_grid = padded_grid[::-1]
# add an extra row so X by X matrix
if len(padded_grid) != stack_max:
    padded_grid.append([''] * stack_max)

# do a diagonal matrix swap
for i in range(stack_max):
    for j in range(i + 1):
        t = padded_grid[i][j]
        padded_grid[i][j] = padded_grid[j][i]
        padded_grid[j][i] = t

# reduce grid from padding
reduced_grid = []
for row in padded_grid:
    new_row = []
    for item in row:
        if item != "":
            new_row.append(item)
    reduced_grid.append(new_row)

instructions = instructions.strip().split('\n')

for instruction in instructions:
    move_num, direction = instruction.split(' from ')
    move_num = int(move_num.split('move ')[1])
    direction = [int(dr) for dr in direction.split(' to ')]
    lifted_boxes = reduced_grid[direction[0]-1][-move_num:]
    reduced_grid[direction[1]-1] += lifted_boxes
    reduced_grid[direction[0]-1] = reduced_grid[direction[0]-1][:-move_num]

print()
[print(row) for row in reduced_grid]


