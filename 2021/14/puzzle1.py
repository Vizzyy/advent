with open('test.txt') as file:
    input_text = file.read().strip().split('\n')

start_polymer = input_text[0]
num_steps = 4

insertion_rules_map = {}
for rule in input_text[2:]:
    split_rule = rule.split(' -> ')
    insertion_rules_map[split_rule[0]] = split_rule[1]

print(f"start_polymer: {start_polymer}")
print(insertion_rules_map)


def do_insertions(input_polymer):
    for rule in insertion_rules_map.keys():
        print(rule)
    return input_polymer


current_polymer = start_polymer

for step in range(1, num_steps + 1):
    current_polymer = do_insertions(current_polymer)
