from datetime import datetime
import math

startTime = datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [input.strip().split('\n') for input in inputs.strip().split('\n\n')]

ordering_rules = [[int(page) for page in input.split('|')] for input in inputs[0]]
page_updates = [[int(page) for page in input.split(',')] for input in inputs[1]]

ordering_map = {}
for rule in ordering_rules:
    if rule[0] not in ordering_map.keys():
        ordering_map[rule[0]] = [rule[1]]
    else:
        ordering_map[rule[0]].append(rule[1])

# [print(input) for input in ordering_rules]
[print(input) for input in page_updates]

print(ordering_map)

correctly_ordered_pages = []

for update in page_updates:
    correctly_ordered = True
    for page_idx in range(len(update)):
        page = update[page_idx]

        if not page in ordering_map.keys():
            print(f'page not in ordering_map: {page}')
            continue

        preceeding_pages = update[:page_idx]

        print(f'update: {update}, page: {page}, preceeding_pages: {preceeding_pages}')

        if any(x in preceeding_pages for x in ordering_map[page]):
            correctly_ordered = False
            break

    print(f'({update}) is correctly ordered? {correctly_ordered}')

    if correctly_ordered:
        correctly_ordered_pages.append(update)

[print(page) for page in correctly_ordered_pages]

total = sum([ordered_pages[math.floor(len(ordered_pages)/2)] for ordered_pages in correctly_ordered_pages])
print(total)

print(f'\nCompletion time: {datetime.now() - startTime}')
