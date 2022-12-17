import math

with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = [[thing.strip().split(' ') for thing in line.split('\n')] for line in inputs.strip().split('\n\n')]

monkeys = {}
ROUNDS_TO_PLAY = 10000

for monkey in inputs:
    # print(monkey)
    monkey_num = int(monkey[0][1].split(':')[0])
    starting_items = [int(item.replace(',', '')) for item in monkey[1][2:]]
    operation_type = monkey[2][4]
    operation_quantity = int(monkey[2][5]) if monkey[2][5].isnumeric() else monkey[2][5]
    test_divisble_by = int(monkey[3][3])
    true_monkey = int(monkey[4][5])
    false_monkey = int(monkey[5][5])
    inspections_count = 0
    monkeys[monkey_num] = {
        'items': starting_items,
        'operation_type': operation_type,
        'operation_quantity': operation_quantity,
        'test_divisble_by': test_divisble_by,
        'true_monkey': true_monkey,
        'false_monkey': false_monkey,
        'inspections_count': inspections_count
    }

# print(monkeys)

divisor = math.prod([monkeys[monkey]['test_divisble_by'] for monkey in monkeys])
print(f'divisor: {divisor}\n')

for i in range(1, ROUNDS_TO_PLAY+1):
    for monkey in monkeys:
        for item in monkeys[monkey]['items'].copy():
            monkeys[monkey]['inspections_count'] = monkeys[monkey]['inspections_count'] + 1

            if monkeys[monkey]['operation_type'] == "*":
                if monkeys[monkey]['operation_quantity'] == 'old':
                    worry_level = item * item
                else:
                    worry_level = item * monkeys[monkey]['operation_quantity']
            else:  # else it is addition
                worry_level = item + monkeys[monkey]['operation_quantity']

            if worry_level > divisor:
                # temp1 = worry_level / divisor
                # temp2 = worry_level // divisor
                worry_level = worry_level % divisor
                # print(temp1, temp2, temp3)

            if worry_level % monkeys[monkey]['test_divisble_by'] == 0:
                monkey_passed_to = monkeys[monkey]['true_monkey']
            else:
                monkey_passed_to = monkeys[monkey]['false_monkey']

            monkeys[monkey_passed_to]['items'].append(worry_level)
            monkeys[monkey]['items'].remove(item)

            # print(f'[{i}], Monkey {monkey}, item: {item}, worry_level: {worry_level}, '
            #       f'pass_gate: {worry_level % monkeys[monkey]["test_divisble_by"] == 0}, '
            #       f'monkey_passed_to: {monkey_passed_to}')

    # print(monkeys)

# [print(monkeys[monkey]['items']) for monkey in monkeys]
[print(monkeys[monkey]['inspections_count']) for monkey in monkeys]


monkey_business = sorted([monkeys[monkey]['inspections_count'] for monkey in monkeys], reverse=True)
print(monkey_business[0] * monkey_business[1])
