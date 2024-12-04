from datetime import datetime
import sys
sys.path.append('../../patterns')
import grid_helpers
import copy


startTime = datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

# print(inputs)

grid = [list(row) for row in inputs]
grid_results = copy.copy(grid)
grid_results = [['.' for col in row] for row in grid]


# [print(row) for row in grid]

appearances_count = 0
directions = [
    'top',
    'bottom',
    'left',
    'right',
    'top_left',
    'top_right',
    'bottom_left',
    'bottom_right'
]


def attempt_consecutive_matches(grid, row, col, direction):
    # assumes we pass in a location of X
    xmas_locations = []
    args = (grid,row,col)
    step_one = grid_helpers.function_map[direction](*args)
#     print(f'step_one: {step_one}')
    if step_one is not None and step_one['val'] == 'M':
        args = (grid,step_one['loc'][0],step_one['loc'][1])
        step_two = grid_helpers.function_map[direction](*args)
#         print(f'step_two: {step_two}')
        if step_two is not None and step_two['val'] == 'A':
            args = (grid,step_two['loc'][0],step_two['loc'][1])
            step_three = grid_helpers.function_map[direction](*args)
#             print(f'step_three: {step_three}')
            if step_three is not None and step_three['val'] == 'S':
                xmas_locations = [
                    [row,col],
                    [step_one['loc'][0],step_one['loc'][1]],
                    [step_two['loc'][0],step_two['loc'][1]],
                    [step_three['loc'][0],step_three['loc'][1]]
                ]
    return xmas_locations


for row_idx in range(len(grid)):
    row = grid[row_idx]

    for col_idx in range(len(grid[row_idx])):
        letter = row[col_idx]

        if letter == 'X':
            for direction in directions:
                matches = attempt_consecutive_matches(grid, row_idx, col_idx, direction)
                if len(matches) > 0:
                    appearances_count += 1
#                     print(f'found {direction} matched word: {matches}')
                    for location in matches:
#                         print(f'location in matches: {location}')
                        grid_results[location[0]][location[1]] = grid[location[0]][location[1]]


# print()
# [print(row) for row in grid_results]
# print()
print(appearances_count)

print(f'\nCompletion time: {datetime.now() - startTime}')
