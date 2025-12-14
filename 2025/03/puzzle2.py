with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split(',')
# print(inputs)
inputs = [[int(item) for item in line.strip().split('-')] for line in inputs]
[print(item) for item in inputs]

