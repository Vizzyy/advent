import sys

import time

import datetime

start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [[[int(part) for part in pair.split(',')] for pair in line.split(' -> ')] for line in
          inputs.strip().split('\n')]


grid_size = 1000
grid = [['.'] * grid_size for i in range(grid_size)]
sand_start = [0, 500]
stop_objects = ['o', '#']
DEPTH_MAX = 200
max_printing_depth = 0
min_printing_col = 800
max_printing_col = 0
round_num = 1
units_at_rest = 0
global_break = False
round_limit = 1000
DEBUG = False


def get_line_points(start, end):
    result = []
    if start[0] == end[0]:
        for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            result.append([start[0], i])
    elif start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            result.append([i, start[1]])
    else:
        print('something is wrong; we cannot have diagonals')
        sys.exit(1)
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
    print(columns)

    # rows_to_print = 170
    min_rows = 0
    # min_rows = max(0, rows_to_print - 30)
    for i in range(min_rows, rows_to_print):
        row = '  '.join(grid[i][column_range[0]:column_range[-1]])
        print(f'[{i:3}] {row}')
    print(columns)


def position_assessment(observer, depth=0):
    if depth == 0:
        if DEBUG: print(f'[position_assessment]: {observer}')
    result = observer.copy()

    if depth > DEPTH_MAX:
        print(f'We have fallen into the abyss...')
        return None

    # down
    if grid[observer[0] + 1][observer[1]] not in stop_objects:
        # print(f'Room to drop down...')
        result = position_assessment([observer[0] + 1, observer[1]], depth + 1)
        return result

    # left
    if grid[observer[0] + 1][observer[1] - 1] not in stop_objects:
        if DEBUG: print(f'Room to drop left...')
        result = position_assessment([observer[0] + 1, observer[1] - 1])
        return result

    # right
    if grid[observer[0] + 1][observer[1] + 1] not in stop_objects:
        if DEBUG: print(f'Room to drop left...')
        result = position_assessment([observer[0] + 1, observer[1] + 1])
        return result

    return result


while not global_break and round_num <= round_limit:
    if DEBUG: print(f'\n[Round {round_num}]')
    sand = sand_start.copy()

    if DEBUG: print(f'Observing from: {sand} ({grid[sand[0]][sand[1]]}) -> next = {grid[sand[0] + 1][sand[1]]}')

    final_position = position_assessment(sand.copy())
    if final_position:
        max_printing_depth = max(max_printing_depth, final_position[0])
        min_printing_col = min(min_printing_col, final_position[1])
        max_printing_col = max(max_printing_col, final_position[1])
        grid[final_position[0]][final_position[1]] = 'o'
        units_at_rest += 1
    else:
        break
    if DEBUG: print(f'final_position: {final_position}')

    # print_grid(max_printing_depth + 5, min_printing_col - 5, max_printing_col + 5)
    round_num += 1

print_grid(max_printing_depth + 5, min_printing_col - 5, max_printing_col + 5)

print(f'units_at_rest: {units_at_rest}')
print(f'elapsed: {datetime.datetime.now() - start}')
