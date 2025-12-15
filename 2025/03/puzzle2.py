with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
# print(inputs)
inputs = [str(line) for line in inputs]
# [print(item) for item in inputs]

highest_joltages = []

for input in inputs:
    indexes = []
    highest = -1
    temp_max = highest
    temp_max_idx = -1

    # first digit must be between indexes 0-3 in order to have space for 12 digits
    for idx in range(len(input)-11):
        potential_max = int(input[idx])

        if potential_max > temp_max:
            temp_max = potential_max
            temp_max_idx = idx

    highest = temp_max
    indexes.append(temp_max_idx)

    # for the remaining 11 digits we can search starting from the first digit to the max index that digit can be (3+i)
    for i in range(1,12):
        max_search_idx = len(input) - (12 - i) + 1

        temp_max = highest
        temp_max_idx = -1
        # search starting right after the previous index up until the maximum location that digit can be
        for idx in range(indexes[i-1]+1, max_search_idx):
            potential_max = ''.join([str(input[index]) for index in indexes])
            potential_max = int(f'{potential_max}{input[idx]}')
            if potential_max > temp_max:
                temp_max = potential_max
                temp_max_idx = idx

        highest = temp_max
        indexes.append(temp_max_idx)

    highest_joltages.append(highest)

print(sum(highest_joltages))