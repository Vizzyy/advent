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

print(f'\nCompletion time: {datetime.now() - startTime}')

walked_map = copy.copy(lab_map)
guard_location = None
guard_directions = ['^','>','v','<']
guard_direction_idx = 0
guard_direction = guard_directions[guard_direction_idx]

for row in range(len(lab_map)):
    if guard_direction in lab_map[row]:
        guard_location = [row, lab_map[row].index(guard_direction)]

walked_map_locations = 1

def get_next_spot(curr_row, curr_col):
    next_spot = None
    if guard_direction == '^':
        next_spot = grid_helpers.get_top(lab_map, curr_row, curr_col)
    elif guard_direction == '>':
        next_spot = grid_helpers.get_right(lab_map, curr_row, curr_col)
    elif guard_direction == 'v':
        next_spot = grid_helpers.get_bottom(lab_map, curr_row, curr_col)
    elif guard_direction == '<':
        next_spot = grid_helpers.get_left(lab_map, curr_row, curr_col)
    return next_spot


# print('Lab Map:')
# [print(row) for row in lab_map]
# print()

counter = 2
while (True):

    # mark current spot on walked map
    walked_map[guard_location[0]][guard_location[1]] = 'X'
    # print('Walked Map:')
    # [print(row) for row in walked_map]

    # get spot in front of guard
    next_spot = get_next_spot(guard_location[0],guard_location[1])
    if next_spot is not None and next_spot['val'] == '#':
        guard_direction_idx = (guard_direction_idx + 1) % 4 # get next direction
        guard_direction = guard_directions[guard_direction_idx]
    elif next_spot is not None:
        guard_location = next_spot['loc']
        lab_map[guard_location[0]][guard_location[1]] = guard_direction
        walked_map_locations += 1
    else:
        break

    # print('Lab Map:')
    # [print(row) for row in lab_map]
    # print()

    # input()


walked_map_locations = sum([row.count('X') for row in walked_map])


print(walked_map_locations)