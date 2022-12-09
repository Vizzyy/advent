with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')
inputs = [[int(char) for char in row] for row in inputs]


def is_visible(row, column):
    spot_height = inputs[row][column]

    if row == 0 or column == 0 or row == len(inputs) - 1 or column == len(inputs[0]) - 1:
        return True
    
    copy_row = row
    copy_column = column - 1
    while True:
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_column -= 1
        if copy_column < 0: 
            return True

    copy_row = row
    copy_column = column + 1
    while True:
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_column += 1
        if copy_column > len(inputs[0]) - 1:
            return True

    copy_row = row - 1
    copy_column = column
    while True:
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_row -= 1
        if copy_row < 0: 
            return True

    copy_row = row + 1
    copy_column = column
    while True:
        if inputs[copy_row][copy_column] >= spot_height:
            break
        copy_row += 1
        if copy_row > len(inputs) - 1:
            return True

    return False 


visible_trees = []
for row in range(len(inputs)):
    for column in range(len(inputs[row])):
        if is_visible(row, column):
            visible_trees.append([row, column])

print(len(visible_trees))