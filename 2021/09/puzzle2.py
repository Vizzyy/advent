with open('test_input.txt', 'r') as file:
    puzzle_input = file.read().strip().split('\n')

puzzle_input = [[int(char) for char in row] for row in puzzle_input]
# [print(row) for row in puzzle_input]


def find_adjacent(x, y):
    result = []
    if x < len(puzzle_input[0]) - 1:  # right adj
        result.append(puzzle_input[y][x+1])
    else:
        result.append(-1)
    if x > 0:  # left adj
        result.append(puzzle_input[y][x-1])
    else:
        result.append(-1)
    if y < len(puzzle_input) - 1:  # down adj
        result.append(puzzle_input[y+1][x])
    else:
        result.append(-1)
    if y > 0:  # up adj
        result.append(puzzle_input[y-1][x])
    else:
        result.append(-1)
    return result


low_points = []

for row_index in range(len(puzzle_input)):
    print(f"row: {row_index}")
    row = puzzle_input[row_index]
    for col_index in range(len(row)):
        number = row[col_index]
        adjacent_numbers = find_adjacent(col_index, row_index)
        # print(adjacent_numbers)
        for adjacent_number in adjacent_numbers:
            if number < adjacent_number or adjacent_number == -1:
                continue
            else:
                number = -1
                break
        if number != -1:
            low_points.append([col_index, row_index, number])

print(low_points)


def find_higher_adjacents(x, y, value):
    basin = []





for low_point in low_points:
    pass
