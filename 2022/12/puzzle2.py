with open('test.txt', 'r') as file:
    grid = file.read()
grid = grid.strip().split('\n')
[print(row) for row in grid]
