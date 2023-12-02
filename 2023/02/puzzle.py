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
    failed = False
    parsed = line.split(': ')[1]
    # print(parsed)
    subsets = [[color.strip() for color in colors.split(',')] for colors in parsed.split(';')]
    # print(subsets)

    for subset in subsets:
        if failed:
            break
        print(subset)
        for pair in subset:
            if failed:
                break
            number, color = pair.split(' ')
            if int(number) > cube_map[color]:
                print('failed')
                failed = True
    
    print('')
    if not failed:
        successful.append(index)
    index += 1

print(sum(successful))
