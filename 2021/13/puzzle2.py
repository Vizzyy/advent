with open('input.txt') as file:
    input_text = file.read().strip().split('\n')

input_text = [[int(coord) for coord in line.split(',')] for line in input_text]

# print(input_text)
# print()

max_x = 0
max_y = 0

for coord in input_text:
    if coord[0] > max_x:
        max_x = coord[0]
    if coord[1] > max_y:
        max_y = coord[1]

max_x += 1
max_y += 1

print(f"max: {max_x}, {max_y}")

paper = [['.' for x in range(max_x)] for y in range(max_y)]

for dot in input_text:
    paper[dot[1]][dot[0]] = '#'

# [print(line) for line in paper]
# print()


def merge(grid_one, grid_two):
    result_grid = [['.' for row in column] for column in grid_one]
    for row in range(len(grid_one)):
        for column in range(len(grid_one[row])):
            if grid_one[row][column] == '#' or grid_two[row][column] == '#':
                result_grid[row][column] = '#'

    return result_grid


def fold_up(current_grid, line_position):
    top_half = current_grid[:line_position]
    bottom_half = current_grid[line_position:]
    bottom_half.reverse()
    return merge(top_half, bottom_half)


def fold_left(current_grid, line_position):
    left_half = []
    right_half = []

    for row in current_grid:
        left_half_row = []
        right_half_row = []
        for column in range(len(row)):
            if column < line_position:
                left_half_row.append(row[column])
            if column > line_position:
                right_half_row.insert(0, row[column])
        left_half.append(left_half_row.copy())
        right_half.append(right_half_row.copy())
        # print(row)
        # print(left_half_row, ' | ', right_half_row)
        # print()

    return merge(left_half, right_half)


# fold along x=655
result_paper = fold_left(paper.copy(), 655)

# [print(line) for line in result_paper]
# print()

count_dots = 0

for row in result_paper:
    for column in row:
        if column == "#":
            count_dots += 1

print(count_dots)

# result_paper = fold_left(result_paper.copy(), 5)
#
# [print(line) for line in result_paper]
# print()

# fold along y=447
result_paper = fold_up(result_paper.copy(), 447)

# fold along x=327
result_paper = fold_left(result_paper.copy(), 327)

# fold along y=223
result_paper = fold_up(result_paper.copy(), 223)

# fold along x=163
result_paper = fold_left(result_paper.copy(), 163)

# fold along y=111
result_paper = fold_up(result_paper.copy(), 111)

# fold along x=81
result_paper = fold_left(result_paper.copy(), 81)

# fold along y=55
result_paper = fold_up(result_paper.copy(), 55)

# fold along x=40
result_paper = fold_left(result_paper.copy(), 40)

# fold along y=27
result_paper = fold_up(result_paper.copy(), 27)

# fold along y=13
result_paper = fold_up(result_paper.copy(), 13)

# fold along y=6
result_paper = fold_up(result_paper.copy(), 6)

[print(line) for line in result_paper]
print()
