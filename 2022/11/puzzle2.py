with open('test.txt', 'r') as file:
    inputs = file.read()
inputs = [line.split('\n') for line in inputs.strip().split('\n\n')]
[print(line) for line in inputs]
