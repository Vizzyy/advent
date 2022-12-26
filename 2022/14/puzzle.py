import time

import datetime

start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [[[int(part) for part in pair.split(',')] for pair in line.split(' -> ')] for line in
          inputs.strip().split('\n')]
# [print(line) for line in inputs]


grid_size = 1000
grid = [['.'] * grid_size for i in range(grid_size)]
sand_start = [0, 500]
stop_objects = ['o', '#']
DEPTH_MAX = 200
max_printing_depth = 0
min_printing_col = 800
max_printing_col = 0


def get_line_points(start, end):
    # print(f'start: {start} - end: {end}')
    result = []
    if start[0] == end[0]:
        for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            result.append([start[0], i])
    elif start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            result.append([i, start[1]])
    else:
        print('something is wrong; we cannot have diagonals')
    return result


for instruction in inputs:
    for pair in range(len(instruction)):
        try:
            line_points = get_line_points(instruction[pair], instruction[pair + 1])
            for point in line_points:
                grid[point[1]][point[0]] = '#'
        except:
            pass

grid[sand_start[0]][sand_start[1]] = '+'


def print_grid(rows_to_print, col_min, col_max):
    print()
    column_range = list(range(col_min, col_max + 1))
    columns = '      ' + ''.join([f'{str(index)[1:3]} ' for index in column_range])
    # print(columns)
    for i in range(rows_to_print):
        row = ''.join(grid[i][column_range[0]:column_range[-1]])
        print(f'[{i:3}] {row}')


def find_diagonal_left(sand_pos):
    left_depth = 1
    down_depth = 1
    while left_depth < DEPTH_MAX:
        print(f'[find_diagonal_left]: sand_pos = {[sand_pos[0] + (down_depth - 1), sand_pos[1] - (left_depth - 1)]} '
              f'- ({left_depth}) - checking: {[sand_pos[0] + down_depth, sand_pos[1] - left_depth]} = '
              f'{grid[sand_pos[0] + down_depth][sand_pos[1] - left_depth]}')
        if grid[sand_pos[0] + down_depth][sand_pos[1] - left_depth] not in stop_objects:
            down_depth += 1

            if grid[sand_pos[0] + down_depth][sand_pos[1] - left_depth] not in stop_objects:
                print(f'We have room to fall down after diagonal left!')

                while down_depth < DEPTH_MAX:
                    if grid[sand_pos[0] + down_depth][sand_pos[1] - left_depth] not in stop_objects:
                        down_depth += 1
                    else:
                        
                        # run it again after reached new depth
                        sand_pos = position_assessment([sand_pos.copy()[0] + (down_depth - 1), sand_pos.copy()[1] - left_depth])
                        if sand_pos:
                            print(f'Reached a depth: {sand_pos[0] + down_depth - 1}. Returning: {sand_pos}')
                        return sand_pos
                if down_depth == DEPTH_MAX:
                    break

            left_depth += 1
        elif left_depth > 1:
            left_depth -= 1
            down_depth -= 1
            return [sand_pos[0] + down_depth, sand_pos[1] - left_depth]
        else:
            return False

    print(f'[find_diagonal_left] - Fell into the abyss!')
    return None


def find_diagonal_right(sand_pos):
    right_depth = 1
    down_depth = 1
    while down_depth < DEPTH_MAX:
        print(f'[find_diagonal_right]: sand_pos = {[sand_pos[0] + (down_depth - 1), sand_pos[1] + (right_depth - 1)]} '
              f'- ({right_depth}) - checking: {[sand_pos[0] + down_depth, sand_pos[1] + right_depth]} = '
              f'{grid[sand_pos[0] + down_depth][sand_pos[1] + right_depth]}')
        if grid[sand_pos[0] + down_depth][sand_pos[1] + right_depth] not in stop_objects:
            down_depth += 1

            if grid[sand_pos[0] + down_depth][sand_pos[1] + right_depth] not in stop_objects:
                print(f'We have room to fall down after diagonal right!')

                while down_depth < DEPTH_MAX:
                    if grid[sand_pos[0] + down_depth][sand_pos[1] + right_depth] not in stop_objects:
                        down_depth += 1
                    else:
                        
                        # run it again after reached new depth
                        sand_pos = position_assessment([sand_pos.copy()[0] + (down_depth - 1), sand_pos.copy()[1] + right_depth])
                        if sand_pos:
                            print(f'Reached a depth: {sand_pos[0] + down_depth - 1}. Returning: {sand_pos}')
                        return sand_pos
                        # break

            right_depth += 1
        elif down_depth > 1:
            right_depth -= 1
            down_depth -= 1
            return [sand_pos[0] + down_depth, sand_pos[1] + right_depth]
        else:
            return False

    print(f'[find_diagonal_right] - Fell into the abyss!')
    return None


def position_assessment(observer):
    global max_printing_col, max_printing_depth, min_printing_col
    print(f'[position_assessment]: {observer}')
    # but diagonal left is available
    if left_option := find_diagonal_left(observer.copy()):
        print(f'[position_assessment] - left_option: {left_option}')

        max_printing_depth = max(max_printing_depth, left_option[0])
        min_printing_col = min(min_printing_col, left_option[1])
        max_printing_col = max(max_printing_col, left_option[1])
        return left_option
    elif left_option is None:
        return None

    # left is unavailable, but diagonal right is available
    if right_option := find_diagonal_right(observer.copy()):
        print(f'[position_assessment] - right_option: {right_option}')

        max_printing_depth = max(max_printing_depth, right_option[0])
        min_printing_col = min(min_printing_col, right_option[1])
        max_printing_col = max(max_printing_col, right_option[1])
        return right_option
    elif right_option is None:
        return None

    # neither side is available, so build up
    else:
        print('[position_assessment] - neither side is available, taking observer position (middle)')

        max_printing_depth = max(max_printing_depth, observer[0])
        min_printing_col = min(min_printing_col, observer[1])
        max_printing_col = max(max_printing_col, observer[1])
        return observer.copy()



round_num = 1
rounds = 25
units_at_rest = 0
global_break = False
round_limit = 2320

while not global_break and round_num <= round_limit:
    print(f'\n[Round {round_num}]')
    sand = sand_start.copy()

    failsafe = rounds * 10
    while failsafe > 0 and not global_break:
        try:
            print(f'Observing from: {sand} ({grid[sand[0]][sand[1]]}) -> next = {grid[sand[0] + 1][sand[1]]}')

            # if next spot is not an obstacle, fall down one space
            if grid[sand[0] + 1][sand[1]] not in stop_objects:
                sand[0] += 1

            # if next spot is going to be an obstacle
            else:
                if (final_position := position_assessment(sand.copy())) is None:
                    global_break = True
                    break
                
                grid[final_position[0]][final_position[1]] = 'o'
                units_at_rest += 1
                break

        except IndexError:
            print(f'Reached end of grid')
            break

        failsafe -= 1

    print_grid(max_printing_depth + 5, min_printing_col - 5, max_printing_col + 5)
    round_num += 1
    # time.sleep(1)

print(f'units_at_rest: {units_at_rest}')
print(f'elapsed: {datetime.datetime.now() - start}')
