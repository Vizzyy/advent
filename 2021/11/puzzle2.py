import copy

with open('input.txt') as file:
    text = file.read().strip().split('\n')

grid = [[int(char) for char in line] for line in text]
grid_max_col = len(grid[0]) - 1
grid_max_row = len(grid) - 1
steps = 0
flash_count = 0


def print_grid(step=None):
    if step is not None:
        print(f"After step {step}:")

    [print(''.join([str(char) for char in row])) for row in grid]
    # [print(row) for row in grid]
    print()


def increment_grid():
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            grid[row][column] += 1


def blooms_exist(bloom_grid):
    for row in range(len(bloom_grid)):
        for column in range(len(bloom_grid[row])):
            if bloom_grid[row][column] > 9:
                return True
    return False


def synchronized(bloom_grid):
    for row in range(len(bloom_grid)):
        for column in range(len(bloom_grid[row])):
            if bloom_grid[row][column] != 0:
                return False
    return True


def find_blooms():
    global flash_count
    bloom_grid = copy.deepcopy(grid)
    keep_going = True

    while keep_going:  # Always assume true on first check
        for row in range(len(bloom_grid)):
            for column in range(len(bloom_grid[row])):
                position_value = bloom_grid[row][column]
                if position_value > 9 and position_value:
                    increment_bloom(get_adjacent_positions([row, column]), bloom_grid)
                    flash_count += 1
                    bloom_grid[row][column] = 0
        keep_going = blooms_exist(bloom_grid)

    return bloom_grid


def increment_bloom(adjacents, bloom_grid):
    for adjacent in adjacents:
        row = adjacent[0]
        col = adjacent[1]
        if bloom_grid[row][col] != 0:
            bloom_grid[row][col] += 1


def finalize_blooms(post_bloom_grid):
    global grid
    for row in range(len(post_bloom_grid)):
        for column in range(len(post_bloom_grid[row])):
            if post_bloom_grid[row][column] > 9:
                post_bloom_grid[row][column] = 0

    grid = copy.deepcopy(post_bloom_grid)


def get_adjacent_positions(initial):
    adjacent_positions = []
    row = initial[0]
    col = initial[1]

    # top left
    if col > 0 and row > 0:
        adjacent_positions.append([row-1, col-1])
    # top middle
    if row > 0:
        adjacent_positions.append([row-1, col])
    # top right
    if col < grid_max_col and row > 0:
        adjacent_positions.append([row-1, col+1])

    # left
    if col > 0:
        adjacent_positions.append([row, col-1])
    # right
    if col < grid_max_col:
        adjacent_positions.append([row, col+1])

    # bottom left
    if col > 0 and row < grid_max_row:
        adjacent_positions.append([row+1, col-1])
    # bottom middle
    if row < grid_max_row:
        adjacent_positions.append([row+1, col])
    # bottom right
    if col < grid_max_col and row < grid_max_row:
        adjacent_positions.append([row+1, col+1])

    # print(f"initial: {initial}, adjacent: {adjacent_positions}")

    return adjacent_positions


def main():
    global steps
    # print_grid()

    while True:
        steps += 1
        increment_grid()
        blooms = find_blooms()
        finalize_blooms(blooms)
        print_grid(steps)
        if synchronized(grid):
            break


main()
