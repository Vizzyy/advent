with open('test.txt', 'r') as file:
    grid = file.read()
grid = [[*row] for row in grid.strip().split('\n')]
[print(''.join(row)) for row in grid]
print()
grid = grid[::-1]

start_pos = None
end_pos = None
IS_DEST_GREATER = False  # false == reverse
RECURSION_LIMIT = 50

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
print()

# [print(row) for row in grid]


def get_possible_directions(current_pos, is_dest_value_greater):
    current_x = current_pos[1]
    current_y = current_pos[0]
    start_value = grid[current_y][current_x]
    possible_directions = []

    try:
        dest_y = current_y
        dest_x = current_x - 1
        dest_value = grid[dest_y][dest_x]
        print(
            f'left: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, {ord(dest_value) <= ord(start_value)}')
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else ord(start_value) - ord(dest_value) <= 1:
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass
    try:
        dest_y = current_y
        dest_x = current_x + 1
        dest_value = grid[dest_y][dest_x]
        print(
            f'right: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, {ord(dest_value) <= ord(start_value)}')
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else ord(start_value) - ord(dest_value) <= 1:
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass
    try:
        dest_y = current_y - 1
        dest_x = current_x
        dest_value = grid[dest_y][dest_x]
        print(
            f'down: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, {ord(dest_value) <= ord(start_value)}')
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else ord(start_value) - ord(dest_value) <= 1:
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass
    try:
        dest_y = current_y + 1
        dest_x = current_x
        dest_value = grid[dest_y][dest_x]
        print(
            f'up: {[dest_y, dest_x]}({ord(dest_value)}), dest_value: {dest_value}, {ord(dest_value) <= ord(start_value)}')
        if ord(dest_value) > ord(start_value) if is_dest_value_greater else ord(start_value) - ord(dest_value) <= 1:
            possible_directions.append([dest_y, dest_x])
    except IndexError:
        pass

    print(f'[get_possible_directions] - current_pos: {current_pos}, start_value: {start_value}({ord(start_value)}), '
          f'possible_directions: {possible_directions}')

    return possible_directions.copy()


def traverse_backwards(current_pos, previous_pos, final_pos, steps_since_beginning):
    possible_directions = get_possible_directions(current_pos, IS_DEST_GREATER)
    print(f'[traverse_backwards] - current_pos: {current_pos}, possible_directions: {possible_directions}, '
          f'steps_since_beginning: {steps_since_beginning}')

    if steps_since_beginning > RECURSION_LIMIT:
        print('We have reached the recursion limit!')
        return

    if current_pos == final_pos:
        print('We have reached the terminus.')
        return

    if f'{current_pos[0]},{current_pos[1]}' in memo:
        print('We have already mapped this location.')
        return

    for possible_direction in possible_directions:
        if previous_pos and possible_direction == previous_pos:  # skip the direction we just came from
            continue
        memo[f'{current_pos[0]},{current_pos[1]}'] = steps_since_beginning + 1
        print(f'possible_direction: {possible_direction}')
        traverse_backwards(possible_direction, current_pos, final_pos, steps_since_beginning + 1)


traverse_backwards(end_pos, None, start_pos, 0)

print()
print(memo)
