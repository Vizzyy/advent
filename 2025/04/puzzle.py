import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'patterns'))
import grid_helpers

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
grid = [[c for c in line] for line in inputs]
# [print(item) for item in grid]

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