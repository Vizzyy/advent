from datetime import datetime
import copy
import sys
sys.path.append('../../patterns')
import grid_helpers

startTime = datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

lab_map = [list(input) for input in inputs]

# [print(row) for row in lab_map]

guard_directions = ['^','>','v','<']
guard_location = None

def get_next_spot(inner_lab_map, curr_row, curr_col, direction):
    next_spot = None
    if direction == '^':
        next_spot = grid_helpers.get_top(inner_lab_map, curr_row, curr_col)
    elif direction == '>':
        next_spot = grid_helpers.get_right(inner_lab_map, curr_row, curr_col)
    elif direction == 'v':
        next_spot = grid_helpers.get_bottom(inner_lab_map, curr_row, curr_col)
    elif direction == '<':
        next_spot = grid_helpers.get_left(inner_lab_map, curr_row, curr_col)
    return next_spot


# print('Lab Map:')
# [print(row) for row in lab_map]
# print()

for row in range(len(lab_map)):
    if '^' in lab_map[row]:
        guard_location = [row, lab_map[row].index('^')]


def test_obstacle(inner_lab_map, obstacle_y, obstacle_x, inner_guard_location):
    inner_lab_map[obstacle_y][obstacle_x] = '#'
    inner_guard_direction_idx = 0
    inner_guard_direction = guard_directions[inner_guard_direction_idx]

    loop_check = 10
    previous_walked_count = 0
    while (True):

        # mark current spot on walked map
        # print('Walked Map:')
        # [print(row) for row in inner_walked_map]

        # get spot in front of guard
        next_spot = get_next_spot(inner_lab_map, inner_guard_location[0],inner_guard_location[1], inner_guard_direction)
        # print(f'inner_guard_location: {inner_guard_location}, inner_guard_direction: {inner_guard_direction}, next_spot: {next_spot}')
        if next_spot is not None and next_spot['val'] == '#':
            # print(f'guard_durection initally: {inner_guard_direction}')
            inner_guard_direction_idx = (inner_guard_direction_idx + 1) % 4 # get next direction
            inner_guard_direction = guard_directions[inner_guard_direction_idx]
            # print(f'guard_durection after: {inner_guard_direction}')
            # continue
        elif next_spot is not None:
            inner_guard_location = next_spot['loc']
            inner_lab_map[inner_guard_location[0]][inner_guard_location[1]] = inner_guard_direction
            # walked_map_locations += 1
        else:
            # print(f'break test_obstacle loop')
            break

        # print('Lab Map:')
        # [print(row) for row in inner_lab_map]
        # print()

        inner_lab_map[inner_guard_location[0]][inner_guard_location[1]] = 'X'

        walked_map_locations = sum([row.count('X') for row in inner_lab_map])
        # print(f'walked_map_locations: {walked_map_locations}')
        if walked_map_locations == previous_walked_count:
            loop_check -= 1
            # print(f'loop_check: {loop_check}')
        
        if loop_check == 0:
            print(f'\Loop time: {datetime.now() - startTime}')
            print(f'Found loopable obstruction @ [{obstacle_y}, {obstacle_x}]')
            return True
        else:
            previous_walked_count = walked_map_locations

        # input()


    # print(f'return False')
    return False


count_loopable = 0

for row in range(len(lab_map)):
    # if row != 6:
    #     print('skipping')
    #     continue
    for col in range(len(lab_map[row])):
        # print(f'{row}, {col}')
        # if input() != 'y':
        #     continue

        # if col != 3:
        #     print('skipping')
        #     continue
        if lab_map[row][col] not in ['^']:
            # print(f'test_obstacle outer: {row},{col}')
            if test_obstacle(copy.deepcopy(lab_map), row, col, copy.deepcopy(guard_location)):
                count_loopable += 1


print(f'count_loopable: {count_loopable}')

print(f'\nCompletion time: {datetime.now() - startTime}')
