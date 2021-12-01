with open('input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# print(sanitized_inputs)

parsed_rules = {}

for rule in sanitized_inputs:
    parsed_rule = rule.split("bags contain ")
    contained_bags = parsed_rule[1].replace(".", "").split(', ')

    # print(contained_bags)

    parsed_rules[parsed_rule[0].strip()] = contained_bags
    # print(parsed_rules[parsed_rule[0]])


def can_hold_color_directly(color):
    color_count = 0
    colors_can_hold_directly = []
    for key in parsed_rules.keys():
        # print(parsed_rules[key])
        rule = parsed_rules[key]
        for sub_rule in rule:
            if color in sub_rule:
                color_count += 1
                colors_can_hold_directly.append(key)
                break
    return colors_can_hold_directly


# print(can_hold_color_directly("shiny gold"))


can_hold_gold = can_hold_color_directly("shiny gold")
can_hold_color_that_holds_gold = [] + can_hold_gold
for color in can_hold_gold:
    can_hold = can_hold_color_directly(color)
    for can_hold_color in can_hold:
        if can_hold_color not in can_hold_color_that_holds_gold:
            can_hold_color_that_holds_gold.append(can_hold_color)

for color in can_hold_color_that_holds_gold:
    can_hold = can_hold_color_directly(color)
    for can_hold_color in can_hold:
        if can_hold_color not in can_hold_color_that_holds_gold:
            can_hold_color_that_holds_gold.append(can_hold_color)

can_hold_color_that_holds_gold.sort()
# print(can_hold_color_that_holds_gold)
print(len(can_hold_color_that_holds_gold))


# part 2

#             1
#         2   3   4
#     2 2     2       0
# 1 1    0    0


def bag_contains(value):
    inner_bag_count = 0
    if "no other" not in ' '.join(value):
        for inner_color in value:
            # print(inner_color)
            count_for_inner = inner_color[0]
            # print(count_for_inner)
            bag_name = inner_color[2:].split(" bag")[0]
            # inner_bag_count += int(inner_color[0])
            # print(bag_name)
            rule_for_inner = parsed_rules[bag_name]
            # print(f"{bag_name}: {rule_for_inner}")
            inner_bag_count += int(count_for_inner) + (int(count_for_inner)*int(bag_contains(rule_for_inner)))
    # else:
    #     print("no other bags!")

    # print(inner_bag_count)
    # print(f"num_mult: {num_mult}")
    return inner_bag_count


print(bag_contains(parsed_rules["shiny gold"]))
