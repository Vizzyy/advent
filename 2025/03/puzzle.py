with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
# print(inputs)
inputs = [str(line) for line in inputs]
# [print(item) for item in inputs]

highest_joltages = []

for input in inputs:
    highest = -1
    idx_left = None
    idx_right = None
    
    print(f"input: {input}")
    for idx in range(len(input)-1):
        print(f"char: {input[idx]} at idx: {idx}")
        if int(input[idx]) > highest:
            highest = int(input[idx])
            idx_left = idx
            print(f"new highest found: {highest} at idx: {idx_left}")

    for idx in range(idx_left, len(input)):
        if idx == idx_left:
            continue
        print(f"char: {input[idx]} at idx: {idx}")
        if int(f'{input[idx_left]}{input[idx]}') > highest:
            highest = int(f'{input[idx_left]}{input[idx]}')
            idx_right = idx
            print(f"new highest found: {highest} at idx: {idx_right}")


    print(f'largest two digit number from {input}: {input[idx_left]}{input[idx_right]} = {highest}')

    highest_joltages.append(highest)

print(highest_joltages)
print(sum(highest_joltages))