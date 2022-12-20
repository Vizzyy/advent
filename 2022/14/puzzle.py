import datetime

start = datetime.datetime.now()

with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = [[pair.split(',') for pair in line.split(' -> ')] for line in inputs.strip().split('\n')]
[print(line) for line in inputs]

print(f'elapsed: {datetime.datetime.now() - start}')
