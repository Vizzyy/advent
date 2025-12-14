import math

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split(',')
# print(inputs)
inputs = [[int(item) for item in line.strip().split('-')] for line in inputs]
[print(item) for item in inputs]

invalid_ids = []

for input in inputs:
    start = input[0] 
    end = input[1]
    for num in range(start, end + 1):
        str_num = str(num)
        # print(str_num)
        left = str_num[:math.floor(len(str_num)/2)]
        right = str_num[math.floor(len(str_num)/2):]
        # print(f"left: {left}, right: {right}")
        if left == right:
            # print(f"invalid id found: {num}")
            invalid_ids.append(num)

print(f'sum: {sum(invalid_ids)}')