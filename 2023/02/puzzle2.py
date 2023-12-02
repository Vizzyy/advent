with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().splitlines()

[print(line) for line in inputs]

cube_map = {
    'red': 12,
    'green': 13,
    'blue': 14
}
index = 1
successful = []
for line in inputs: 
    min_cube_map = {
        'red': [],
        'green': [],
        'blue': []
    }
    parsed = line.split(': ')[1]
    # print(parsed)
    subsets = [[color.strip() for color in colors.split(',')] for colors in parsed.split(';')]
    # print(subsets)

    for subset in subsets:
        print(subset)
        for pair in subset:
            number, color = pair.split(' ')
            min_cube_map[color].append(int(number))
    
    print(min_cube_map)
    max_red = sorted(min_cube_map['red'])[-1]
    max_green = sorted(min_cube_map['green'])[-1]
    max_blue = sorted(min_cube_map['blue'])[-1]
    print(max_red, max_green, max_blue)
    successful.append(max_red * max_green * max_blue)
    index += 1


print(sum(successful))
