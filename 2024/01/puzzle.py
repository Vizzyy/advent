with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

left = []
right = []
for input in inputs:
    pair = input.split(' ')
    left.append(int(pair[0].strip()))
    right.append(int(pair[3].strip()))

# left = list(set(left))
# right = list(set(right))

left.sort()
right.sort()

total_delta = 0
for i in range(len(left)):
    total_delta += abs(left[i] - right[i])

print(total_delta)