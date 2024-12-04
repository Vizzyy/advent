from datetime import datetime
import sys
sys.path.append('../../patterns')
import grid_helpers
import copy


startTime = datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

grid = [list(row) for row in inputs]
grid_results = copy.copy(grid)
grid_results = [['.' for col in row] for row in grid]

appearances_count = 0


def attempt_consecutive_matches(grid, row, col):
    # assumes we pass in a location of A
    # grab all four diagonally adjacent letters
    # return all letter locations (not required)
    xmas_locations = []
    args = (grid,row,col)
    top_left = grid_helpers.function_map['top_left'](*args)
    top_right = grid_helpers.function_map['top_right'](*args)
    bottom_left = grid_helpers.function_map['bottom_left'](*args)
    bottom_right = grid_helpers.function_map['bottom_right'](*args)

    # check if:
    # 1. all four locations are not None
    # 2. the four locations are one of the four acceptable configurations (MS/MS, SS/MM, MM/SS, SM/SM)
    if (top_left is not None and top_right is not None and bottom_left is not None and bottom_right is not None) and \
        ((top_left['val'] == 'M' and top_right['val'] == 'M' and bottom_left['val'] == 'S' and bottom_right['val'] == 'S') \
        or (top_left['val'] == 'M' and top_right['val'] == 'S' and bottom_left['val'] == 'M' and bottom_right['val'] == 'S') \
        or (top_left['val'] == 'S' and top_right['val'] == 'M' and bottom_left['val'] == 'S' and bottom_right['val'] == 'M') \
        or (top_left['val'] == 'S' and top_right['val'] == 'S' and bottom_left['val'] == 'M' and bottom_right['val'] == 'M')):

        xmas_locations = [
                        [row,col],
                        [top_left['loc'][0],top_left['loc'][1]],
                        [top_right['loc'][0],top_right['loc'][1]],
                        [bottom_left['loc'][0],bottom_left['loc'][1]],
                        [bottom_right['loc'][0],bottom_right['loc'][1]]
        ]

    return xmas_locations


for row_idx in range(len(grid)):
    row = grid[row_idx]

    for col_idx in range(len(grid[row_idx])):
        letter = row[col_idx]

        # check for permutations of the "cross" at every location of A
        if letter == 'A':
            matches = attempt_consecutive_matches(grid, row_idx, col_idx)
            if len(matches) > 0:
                appearances_count += 1
                # update our result grid (matches visual example in problem description) (not required)
                for location in matches:
                    grid_results[location[0]][location[1]] = grid[location[0]][location[1]]


print(appearances_count)

print(f'\nCompletion time: {datetime.now() - startTime}')

# Result:
# 1888

# Completion time: 0:00:00.017384
