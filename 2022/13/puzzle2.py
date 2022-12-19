import datetime
import sys
sys.setrecursionlimit(3000)
start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    grid = file.read()
grid = [[*row] for row in grid.strip().split('\n')]
grid = grid[::-1]

start_pos = None
end_pos = None
IS_DEST_GREATER = False  # false == reverse
RECURSION_LIMIT = 900
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

all_possible_start_positions = []
for row in range(len(grid)):
    all_possible_start_positions.append([row, 0])

print(f'start_pos: {start_pos}, end_pos: {end_pos}, possible start locations: {len(all_possible_start_positions)}')
if DEBUG:
    print(all_possible_start_positions)


def append_possibility(dest_y, dest_x, start_value, is_dest_value_greater, direction, possible_directions):
    try:
        if dest_y >= len(grid) or dest_y < 0 or dest_x >= len(grid[0]) or dest_x < 0:
            raise IndexError
        dest_value = grid[dest_y][dest_x]

        if ord(dest_value) - ord(start_value) >= -1:
            # if ord(start_value) - ord(dest_value) <= 1:
            if DEBUG:
                print(f'{direction}: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, '
                      f'{ord(dest_value) <= ord(start_value)}')
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass

    return possible_directions.copy()


def get_possible_directions(current_pos, is_dest_value_greater):
    current_x = current_pos[1]
    current_y = current_pos[0]
    start_value = grid[current_y][current_x]
    possible_directions = []
    if DEBUG:
        print(f'\n[get_possible_directions] - current_pos: {current_pos}, '
              f'start_value: {start_value}({ord(start_value)})')

    dest_y = current_y
    dest_x = current_x - 1
    direction = "left"
    possible_directions = append_possibility(dest_y, dest_x, start_value, is_dest_value_greater, direction,
                                             possible_directions)
    dest_y = current_y
    dest_x = current_x + 1
    direction = "right"
    possible_directions = append_possibility(dest_y, dest_x, start_value, is_dest_value_greater, direction,
                                             possible_directions)
    dest_y = current_y - 1
    dest_x = current_x
    direction = "down"
    possible_directions = append_possibility(dest_y, dest_x, start_value, is_dest_value_greater, direction,
                                             possible_directions)
    dest_y = current_y + 1
    dest_x = current_x
    direction = "up"
    possible_directions = append_possibility(dest_y, dest_x, start_value, is_dest_value_greater, direction,
                                             possible_directions)

    return possible_directions.copy()


def traverse_backwards(current_pos, final_pos, path_traversed):
    global memo, IS_DEST_GREATER
    steps_since_beginning = len(path_traversed)
    previous_pos = path_traversed[-1] if steps_since_beginning > 0 else None
    internal_path = path_traversed.copy()
    internal_path.append(current_pos)
    if DEBUG:
        print(f'\n[traverse] - current: {current_pos}, prev: {previous_pos}, '
              f'path: {internal_path}, steps: {steps_since_beginning}')
    possible_directions = get_possible_directions(current_pos, IS_DEST_GREATER)
    if previous_pos and previous_pos in possible_directions:
        possible_directions.pop(possible_directions.index(previous_pos))
    if DEBUG:
        print(f'possible: {possible_directions}')

    # if it doesn't exist in memo, add it
    if f'{current_pos[0]},{current_pos[1]}' not in memo.keys():
        memo[f'{current_pos[0]},{current_pos[1]}'] = internal_path.copy()
    # else if the current path is less than what is there, overwrite it
    elif len(internal_path) < len(memo[f'{current_pos[0]},{current_pos[1]}']):
        memo[f'{current_pos[0]},{current_pos[1]}'] = internal_path.copy()
        # print('overwriting memo')
    else:
        # print('return due to memo')
        return

    if current_pos in final_pos:
        if DEBUG:
            print(f'We have reached a terminus: {current_pos}.')
        return

    for possible_direction in possible_directions:
        if possible_direction in path_traversed:
            # print(f'Skipping {possible_direction} as it is already part of our path.')
            continue

        if DEBUG:
            print(f'next direction: {possible_direction}')
        traverse_backwards(possible_direction, final_pos, internal_path.copy())


traverse_backwards(end_pos, all_possible_start_positions, [])

if DEBUG:
    print()
    print(memo.keys())

    # print()
    # [print(f'{key}: {memo[key]}, {len(memo[key])}') for key in memo]

    # for step in range(len(path_to_final)):
    #     grid[path_to_final[step][0]][path_to_final[step][1]] = f'{step:2}'
    #
    # print()
    # [print(row) for row in grid[::-1]]

fewest_steps = 100000000
try:
    for terminus in all_possible_start_positions:
        path_to_final = memo[f'{terminus[0]},{terminus[1]}'][1:]
        if len(path_to_final) < fewest_steps:
            fewest_steps = len(path_to_final)
        print(f'\n{terminus} - {path_to_final}, {len(path_to_final)}')
except KeyError:
    pass

print(f'fewest_steps: {fewest_steps}')
print(f'elapsed: {datetime.datetime.now() - start}')

# elapsed: 0:01:41.384512

