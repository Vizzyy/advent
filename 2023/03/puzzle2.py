with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().splitlines()
inputs = [list(input) for input in inputs]

# [print(line) for line in inputs]
# print()

digits_chars = ['1','2','3','4','5','6','7','8','9','0']
ignored_symbols = digits_chars + ['.']
# print(ignored_symbols)

# number_map will be [ [full number, array of digit locations], []... etc ]
number_map = []
for row in range(len(inputs)):
    new_number = ''
    new_number_positions = []
    for col in range(len(inputs[row])):
        char = inputs[row][col]
        # print(f'<{col}> [{range(len(inputs[row]))}] - "{char}"')
        if char in digits_chars:
            new_number += char
            new_number_positions.append([row,col])
            if col == len(inputs[row]) - 1:
                # flush if end of row
                # print(f'{new_number} - {new_number_positions}')
                number_map.append([int(new_number), new_number_positions.copy()])
                new_number = ''
                new_number_positions = [] 
        elif new_number != '':
            # flush
            # print(f'{new_number} - {new_number_positions}')
            number_map.append([int(new_number), new_number_positions.copy()])
            new_number = ''
            new_number_positions = []
            # input()
        else:
            continue

# print(f'number_map: {number_map}')
# [print(entry) for entry in number_map]
# print(len(number_map))


def get_surrounding_spots(y, x):
    result = []

    # top left
    if y - 1 >= 0 and x - 1 >= 0:
        result.append([y-1,x-1])
    # top
    if y - 1 >= 0:
        result.append([y-1,x])
    # top right
    if y - 1 >= 0 and x + 1 < len(inputs[y]):
        result.append([y-1,x+1])
    # left
    if x - 1 >= 0:
        result.append([y,x-1])        
    # right
    if x + 1 < len(inputs[y]):
        result.append([y,x+1])
    # bottom left
    if y + 1 < len(inputs) and x - 1 >= 0:
        result.append([y+1,x-1])
    # bottom 
    if y + 1 < len(inputs):
        result.append([y+1,x])   
    # bottom right
    if y + 1 < len(inputs) and x + 1 < len(inputs[y+1]):
        result.append([y+1,x+1])

    return result


punctuation_spots = []

for row in range(len(inputs)):
    for col in range(len(inputs[row])):
        if inputs[row][col] == "*":
            punctuation_spots.append([row,col])

print()
print(f'punctuation_spots: {punctuation_spots}')
print()

total = 0
stopper = 0
number_map_copy = number_map.copy()

for target in punctuation_spots:
    gears_attached = []
    stopper += 1
    adjacents = get_surrounding_spots(target[0], target[1])
    # print(f'adjacents: {adjacents}')
    for coord in adjacents:
        # print(f'coord in adjacents: {coord}')
        for position in range(len(number_map_copy)):
            number = number_map_copy[position]
            number_value = number[0]
            number_coords = number[1]
            # print(number)
            if coord in number_coords:
                gears_attached.append(number_value) 
                print(f'<{stopper}> found {coord} in {number_coords}, adding {number_value}, total = {total}')
                del number_map_copy[position]
                break
    if len(gears_attached) == 2:
        total += (gears_attached[0] * gears_attached[1])

    # if stopper % 10 == 0:
    #     value = input()
        
print(f'len(punctuation_spots): {len(punctuation_spots)}')
print(total)