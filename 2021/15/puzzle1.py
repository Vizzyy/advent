with open('test.txt') as file:
    input_text = file.read().strip().split('\n')

input_text = [[*row] for row in input_text]

[print(row) for row in input_text]


