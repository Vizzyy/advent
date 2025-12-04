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
    print(f'direction: {direction}, distance: {distance}, position_index: {position_index}')
    
    if direction == 'L':
        if position_index - distance < 0:
            position_index = 100 - (((distance - position_index) % 100) or 1)
        else:
            position_index = position_index - distance
    
    if direction == 'R':
        position_index = (position_index + distance) % 100

    # pass_go = math.floor(distance / 100)
    # zero_pos_count += pass_go

    position_index = dial[position_index]

    if position_index == 0:
        zero_pos_count += 1

    # print(f'new position: {position_index}, pass_go: {pass_go}, zero_pos_count: {zero_pos_count}\n')

    # if zero_pos_count > 20:
    #     break
    if zero_pos_count > 0 and zero_pos_count % 10 == 0:
        input()

print(f'new position: {position_index}')

print(zero_pos_count)