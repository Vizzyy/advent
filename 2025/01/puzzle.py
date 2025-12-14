import math

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
inputs = [[line[0], int(line[1:])] for line in inputs]
# print(inputs)

dial = [num for num in range(100)]
print(dial)

position_index = 50
zero_pos_count = 0

for instruction in inputs:
    direction = instruction[0]
    distance = instruction[1]
    print(f'start position: {position_index}, direction: {direction}, distance: {distance}')
    
    if direction == 'L':
        if position_index - distance < 0:
            position_index = (100 - abs(position_index - distance)) % 100
        else:
            position_index = position_index - distance
    
    if direction == 'R':
        position_index = (position_index + distance) % 100

    if position_index == 0:
        zero_pos_count += 1


print(zero_pos_count)