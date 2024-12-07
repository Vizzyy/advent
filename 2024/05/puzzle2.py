with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

print(inputs)

[print(input) for input in inputs]
