with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')
inputs = [[int(char) for char in row] for row in inputs]

print(inputs)