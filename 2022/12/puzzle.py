with open('test.txt', 'r') as file:
    grid = file.read()
grid = [[*row] for row in grid.strip().split('\n')]
# [print(''.join(row)) for row in grid]
# print()
grid = grid[::-1]

start_pos = None
end_pos = None
IS_DEST_GREATER = False  # false == reverse
RECURSION_LIMIT = 50
shortest_path = None
DEBUG = False

memo = {}

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == 'S':
            start_pos = [row, column]
            grid[row][column] = 'a'
        if grid[row][column] == 'E':
            end_pos = [row, column]
            grid[row][column] = 'z'
    if start_pos and end_pos:
        break

print(f'start_pos: {start_pos}, end_pos: {end_pos}')

# [print(row) for row in grid]


def get_possible_directions(current_pos, is_dest_value_greater):
    current_x = current_pos[1]
    current_y = current_pos[0]
    start_value = grid[current_y][current_x]
    possible_directions = []
    if DEBUG: print(f'\n[get_possible_directions] - current_pos: {current_pos}, start_value: {start_value}({ord(start_value)})')

    try:
        dest_y = current_y
        dest_x = current_x - 1
        if dest_y >= len(grid) or dest_y < 0 or dest_x >= len(grid[0]) or dest_x < 0:
            raise IndexError
        dest_value = grid[dest_y][dest_x]
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else abs(ord(start_value) - ord(dest_value)) <= 1:
            if DEBUG: print(f'left: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, '
                  f'{ord(dest_value) <= ord(start_value)}')
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass
    try:
        dest_y = current_y
        dest_x = current_x + 1
        if dest_y >= len(grid) or dest_y < 0 or dest_x >= len(grid[0]) or dest_x < 0:
            raise IndexError
        dest_value = grid[dest_y][dest_x]
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else abs(ord(start_value) - ord(dest_value)) <= 1:
            if DEBUG: print(f'right: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, '
                  f'{ord(dest_value) <= ord(start_value)}')
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass
    try:
        dest_y = current_y - 1
        dest_x = current_x
        if dest_y >= len(grid) or dest_y < 0 or dest_x >= len(grid[0]) or dest_x < 0:
            raise IndexError
        dest_value = grid[dest_y][dest_x]
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else abs(ord(start_value) - ord(dest_value)) <= 1:
            if DEBUG: print(f'down: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, '
                  f'{ord(dest_value) <= ord(start_value)}')
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass
    try:
        dest_y = current_y + 1
        dest_x = current_x
        if dest_y >= len(grid) or dest_y < 0 or dest_x >= len(grid[0]) or dest_x < 0:
            raise IndexError
        dest_value = grid[dest_y][dest_x]
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else abs(ord(start_value) - ord(dest_value)) <= 1:
            if DEBUG: print(f'up: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, '
                  f'{ord(dest_value) <= ord(start_value)}')
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass

    return possible_directions.copy()


def traverse_backwards(current_pos, final_pos, path_traversed):
    global memo
    steps_since_beginning = len(path_traversed)
    previous_pos = path_traversed[-1] if steps_since_beginning > 0 else None
    internal_path = path_traversed.copy()
    internal_path.append(current_pos)
    if DEBUG: print(f'\n[traverse] - current: {current_pos}, prev: {previous_pos}, path: {internal_path}, steps: {steps_since_beginning}')
    possible_directions = get_possible_directions(current_pos, IS_DEST_GREATER)
    if previous_pos and previous_pos in possible_directions:
        possible_directions.pop(possible_directions.index(previous_pos))
    if DEBUG: print(f'possible: {possible_directions}')

    if steps_since_beginning > RECURSION_LIMIT:
        if DEBUG: print('We have reached the recursion limit!')
        return

    if current_pos == final_pos:
        if DEBUG: print('We have reached the terminus.')

        # if it doesn't exist in memo, add it
        if f'{current_pos[0]},{current_pos[1]}' not in memo.keys():
            memo[f'{current_pos[0]},{current_pos[1]}'] = internal_path.copy()
        # else if the current path is less than what is there, overwrite it
        elif len(internal_path) < len(memo[f'{current_pos[0]},{current_pos[1]}']):
            memo[f'{current_pos[0]},{current_pos[1]}'] = internal_path.copy()

        return

    for possible_direction in possible_directions:
        if possible_direction in path_traversed:
            # print(f'Skipping {possible_direction} as it is already part of our path.')
            continue

        # if it doesn't exist in memo, add it
        if f'{current_pos[0]},{current_pos[1]}' not in memo.keys():
            memo[f'{current_pos[0]},{current_pos[1]}'] = internal_path.copy()
        # else if the current path is less than what is there, overwrite it
        elif len(internal_path) < len(memo[f'{current_pos[0]},{current_pos[1]}']):
            memo[f'{current_pos[0]},{current_pos[1]}'] = internal_path.copy()

        if DEBUG: print(f'next direction: {possible_direction}')
        traverse_backwards(possible_direction, final_pos, internal_path.copy())


traverse_backwards(end_pos, start_pos, [])

# print()
# [print(f'{key}: {memo[key]}, {len(memo[key])}') for key in memo]

# step = 1
# for key in memo.keys():
#     row, column = key.split(',')
#     print(row, column)
#     grid[int(row)][int(column)] = f'{step:2}'
#     step += 1
#
# [print(row) for row in grid]

path_to_final = memo[f'{start_pos[0]},{start_pos[1]}'][1:]
# for step in range(len(path_to_final)):
#     grid[path_to_final[step][0]][path_to_final[step][1]] = f'{step:2}'
#
# print()
# [print(row) for row in grid[::-1]]

print()
print(f'{path_to_final}, {len(path_to_final)}')
