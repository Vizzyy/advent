def get_surrounding_spots(grid, y, x):
    # assumes that grid is a 2D grid, where Y is the index in grid (row), and X is the index in Y (col)

    result = []
    result.append(get_top_left(grid, y, x))
    result.append(get_top(grid, y, x))
    result.append(get_top_right(grid, y, x))
    result.append(get_left(grid, y, x))    
    result.append(get_right(grid, y, x))
    result.append(get_bottom_left(grid, y, x))
    result.append(get_bottom(grid, y, x)) 
    result.append(get_bottom_right(grid, y, x))       

    return result


def get_top_left(grid,y,x):
    # top left
    # return value + grid location of found value
    if y - 1 >= 0 and x - 1 >= 0:
        return {'val': grid[y-1][x-1], 'loc': [y-1,x-1]}
    

def get_top(grid,y,x):    
    # top
    if y - 1 >= 0:
        return {'val': grid[y-1][x], 'loc': [y-1,x]}


def get_top_right(grid,y,x):
    # top right
    if y - 1 >= 0 and x + 1 < len(grid[y]):
        return {'val': grid[y-1][x+1], 'loc': [y-1,x+1]}


def get_left(grid,y,x):
    # left
    if x - 1 >= 0:
        return {'val': grid[y][x-1], 'loc': [y,x-1]}


def get_right(grid,y,x):
    # right
    if x + 1 < len(grid[y]):
        return {'val': grid[y][x+1], 'loc': [y,x+1]}


def get_bottom_left(grid,y,x):
    # bottom left
    if y + 1 < len(grid) and x - 1 >= 0:
        return {'val': grid[y+1][x-1], 'loc': [y+1,x-1]}


def get_bottom(grid,y,x):
    # bottom 
    if y + 1 < len(grid):
        return {'val': grid[y+1][x], 'loc': [y+1,x]}


def get_bottom_right(grid,y,x):
    # bottom right
    if y + 1 < len(grid) and x + 1 < len(grid[y+1]):
        return {'val': grid[y+1][x+1], 'loc': [y+1,x+1]}


function_map = {
    'top_left'      : get_top_left,
    'top'           : get_top,
    'top_right'     : get_top_right,
    'left'          : get_left,
    'right'         : get_right,
    'bottom_left'   : get_bottom_left,
    'bottom'        : get_bottom,
    'bottom_right'  : get_bottom_right,
}