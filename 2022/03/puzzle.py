with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')

total = 0
for rucksack in inputs:
    ruck = rucksack[:int(len(rucksack)/2)]
    sack = rucksack[int(len(rucksack)/2):]
    intersect = list(set(ruck).intersection(sack))[0]
    total += ord(intersect.lower()) - 96 if intersect.islower() else (26 + ord(intersect.lower()) - 96)

print(total)
