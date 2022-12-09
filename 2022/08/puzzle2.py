import math

with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')
inputs = [[int(char) for char in row] for row in inputs]


def is_visible(row, column):
    spot_height = inputs[row][column]
    scores = [0, 0, 0, 0]
    
    copy_row = row
    copy_column = column - 1
    while copy_column >= 0:
        scores[0] += 1
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_column -= 1

    copy_row = row
    copy_column = column + 1
    while copy_column <= len(inputs[0]) - 1:
        scores[1] += 1
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_column += 1

    copy_row = row - 1
    copy_column = column
    while copy_row >= 0:
        scores[2] += 1
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_row -= 1

    copy_row = row + 1
    copy_column = column
    while copy_row <= len(inputs) - 1:
        scores[3] += 1
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_row += 1

    return math.prod(scores) 


highest_score = 0
for row in range(len(inputs)):
    for column in range(len(inputs[row])):
        current_score = is_visible(row, column)
        if current_score > highest_score:
            print(f'new highscore: {[column, row]}')
            highest_score = current_score

print(highest_score)