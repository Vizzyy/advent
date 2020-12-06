from functools import reduce

with open('./input.txt', 'r') as file:
    text = file.read()

inputs = text.split('\n\n')

# print(inputs)

sanitized_inputs = []

for input in inputs:
    temp = input.split('\n')
    sanitized_inputs.append(temp)

# print(sanitized_inputs)

# part one
total_count = 0
for group in sanitized_inputs:
    group_unique_answers = []
    for person in group:
        answers = [char for char in person]
        answers.sort()
        for answer in answers:
            if answer not in group_unique_answers:
                group_unique_answers.append(answer)
    total_count += len(group_unique_answers)

print(total_count)

#part two

total_count = 0
for group in sanitized_inputs:
    group_unique_answers = {}
    print(group)
    intersect = list(reduce(set.intersection, [set(item) for item in group ]))
    print(intersect)
    total_count += len(intersect)
    # break

print(total_count)