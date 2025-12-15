import sys
from pathlib import Path
import copy

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'patterns'))
import grid_helpers

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
main_grid = [[c for c in line] for line in inputs]
rolls_removed = []

while True:
    # [print(item) for item in main_grid]
    grid = copy.deepcopy(main_grid)
    rolls_accessible = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]
            if cell == '@':
                neighbors = grid_helpers.get_surrounding_spots(grid, row, col)
                # print(f'Cell ({row}, {col}) has neighbors: {neighbors}')
                adjacent_rolls = 0
                for neighbor in neighbors:
                    # print(f'Checking neighbor: {neighbor}')
                    if not neighbor:
                        continue
                    if neighbor['val'] == '@':
                        adjacent_rolls += 1
                if adjacent_rolls < 4:
                    rolls_accessible.append((row, col))

    print(f'Number of accessible rolls: {len(rolls_accessible)}')

    for accessible_roll in rolls_accessible:
        rolls_removed.append(accessible_roll)
        row, col = accessible_roll
        main_grid[row][col] = 'x'

    if len(rolls_accessible) == 0:
        break


print(f'Total rolls removed: {len(rolls_removed)}')