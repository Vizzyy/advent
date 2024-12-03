with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().splitlines()

[print(line) for line in inputs]