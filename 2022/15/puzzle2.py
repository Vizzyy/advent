import datetime

start = datetime.datetime.now()

with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

print(inputs)

print(f'elapsed: {datetime.datetime.now() - start}')
