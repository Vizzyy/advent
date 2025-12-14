import math

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
inputs = [[line[0], int(line[1:])] for line in inputs]
# print(inputs)

dial = [num for num in range(100)]
# print(dial)

position_index = 50
zero_pos_count = 0

for instruction in inputs:
    start_index = position_index
    pass_go = 0
    direction = instruction[0]
    distance = instruction[1]
    print(f'start position: {position_index}, direction: {direction}, distance: {distance}')
    
    if direction == 'L':
        if position_index - distance < 0:
            if position_index != 0:
                if distance <= 100:
                    pass_go = 1
                else:
                    pass_go = math.floor(distance / 100)
            else:
                pass_go += math.floor(distance / 100)
            position_index = (100 - abs(position_index - distance)) % 100
        else:
            position_index = position_index - distance
    
    if direction == 'R':
        if position_index + distance >= 100: 
            if position_index != 0:
                if distance >= 100:
                    pass_go = math.floor(distance / 100)
                    if (distance % 100) + position_index > 100:
                        pass_go += 1
                else:
                    if (position_index + distance) % 100 != 0:
                        pass_go = 1
            else:
                pass_go += math.floor(distance / 100)
        position_index = (position_index + distance) % 100

    zero_pos_count += pass_go

    if position_index == 0 and start_index != 0:
        zero_pos_count += 1

    print(f'end position: {position_index}, pass_go: {pass_go}, zero_pos_count: {zero_pos_count} \n')


print(zero_pos_count)

# 6204 (wrong)
# 7120 (not submitted yet)
# 6649 (wrong)
# 6734 (wrong)
