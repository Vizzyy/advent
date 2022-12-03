with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

groups_of_three = list(map(lambda *x: x, *([iter(inputs)] * 3)))

total = 0
for group in groups_of_three:
    intersect = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
    total += ord(intersect.lower()) - 96 if intersect.islower() else (26 + ord(intersect.lower()) - 96)

print(total)
