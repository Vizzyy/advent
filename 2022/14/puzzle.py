import datetime

start = datetime.datetime.now()

with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = [[pair.split(',') for pair in line.split(' -> ')] for line in inputs.strip().split('\n')]
[print(line) for line in inputs]


grid = [''] * 1000
grid = [grid.copy()] * 1000

for instruction in inputs:
    for pair in range(len(instruction)):
        column = instruction[pair][0]
        row = instruction[pair][1]
        print(column, row)

print(f'elapsed: {datetime.datetime.now() - start}')
