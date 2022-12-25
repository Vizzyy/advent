import datetime

start = datetime.datetime.now()

with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = [[[int(part) for part in pair.split(',')] for pair in line.split(' -> ')] for line in inputs.strip().split('\n')]
[print(line) for line in inputs]


grid_size = 1000
grid = [ ['.']*grid_size for i in range(grid_size)]
sand_start = [0, 500]

def get_line_points(start, end):
    print(f'start: {start} - end: {end}')
    result = []
    if start[0] == end[0]:
        for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            result.append([start[0], i])
    elif start[1] == end[1]:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            result.append([i, start[1]])
    else:
        print('something is wrong; we cannot have diagonals')
    print(result)
    return result

for instruction in inputs:
    for pair in range(len(instruction)):
        try:
            line_points = get_line_points(instruction[pair], instruction[pair + 1])
            for point in line_points:
                grid[point[1]][point[0]] = '#'
        except Exception as e:
            # print(f'{type(e).__name__} - {e}')
            pass

grid[sand_start[0]][sand_start[1]] = '+'


def print_grid():
    print()
    for i in range(10):
        row = ' '.join(grid[i][494:504])
        print(f'[{i}] - {row}')


print_grid()


rounds = 3
stop_objects = ['o', '#']
for i in range(rounds):
    print(f'\n[Round {i + 1}]')
    sand = sand_start.copy()
    failsafe = rounds * 10
    while failsafe > 0:
        try:
            # if the spot below is not a blocker, then fall down one 
            if grid[sand[0] + 1][sand[1]] not in stop_objects:
                sand[0] += 1
                print(f'sand[0] += 1: {sand[0]}')
            else:
                done = False
                # if grid[sand[0] + 1][sand[1]] in stop_objects:
                #     print(f'middle spot good')
                #     done = True
                
                # try left 
                left_failsafe = 2 
                while not done and left_failsafe > 0:
                    print(f'grid[sand[0] + 1][sand[1] - 1]: {grid[sand[0] + 1][sand[1] - 1]}, left_failsafe: {left_failsafe}')
                    if grid[sand[0] + 1][sand[1] - 1] not in stop_objects:
                        sand[0] += 1
                        sand[1] -= 1
                    else:
                        left_failsafe -= 1
                        continue


                    if left_failsafe > 0:
                        done = True
                    else:
                        break

                # else try right
                right_failsafe = rounds * 10 
                while not done and right_failsafe > 0:
                    if grid[sand[0] + 1][sand[1] + 1] not in stop_objects:
                        sand[0] += 1
                        sand[1] += 1
                    
                # else just current position
                grid[sand[0]][sand[1]] = 'o'
                break
        except IndexError:
            print(f'Reached end of grid')
        
        failsafe -= 1

    print_grid()




print(f'elapsed: {datetime.datetime.now() - start}')


