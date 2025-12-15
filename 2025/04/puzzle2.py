with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
# print(inputs)
inputs = [[c for c in line] for line in inputs]
[print(item) for item in inputs]


