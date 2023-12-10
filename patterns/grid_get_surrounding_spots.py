def get_surrounding_spots(grid, y, x):
    # assumes that grid is a 2D grid, where Y is the index in grid (row), and X is the index in Y (col)

    result = []

    # top left
    if y - 1 >= 0 and x - 1 >= 0:
        result.append(grid[y-1][x-1])
    # top
    if y - 1 >= 0:
        result.append(grid[y-1][x])
    # top right
    if y - 1 >= 0 and x + 1 < len(grid[y]):
        result.append(grid[y-1][x+1])
    # left
    if x - 1 >= 0:
        result.append(grid[y][x-1])        
    # right
    if x + 1 < len(grid[y]):
        result.append(grid[y][x+1])
    # bottom left
    if y + 1 < len(grid) and x - 1 >= 0:
        result.append(grid[y+1][x-1])       
    # bottom 
    if y + 1 < len(grid):
        result.append(grid[y+1][x])   
    # bottom right
    if y + 1 < len(grid) and x + 1 < len(grid[y+1]):
        result.append(grid[y+1][x+1])       

    return result