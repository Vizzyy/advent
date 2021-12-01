with open('input.txt', 'r') as file:
    inputs = file.readlines()

fields = []
my_ticket = None
nearby_tickets = []

for i in range(len(inputs)):
    if i < 20:
        fields.append(inputs[i].strip())
    elif i == 22:
        my_ticket = inputs[i].strip().split(',')
    elif i > 24:
        temp = inputs[i].strip().split(',')
        temp = [int(item) for item in temp]
        nearby_tickets.append(temp)

parsed_fields = {}

for field in fields:
    line = field.split(': ')
    temp = line[1].split(' or ')
    result = temp[0].split('-') + temp[1].split('-')
    result = [int(r) for r in result]
    parsed_fields[line[0]] = result


# [print(f"{key} - {parsed_fields[key]}") for key in parsed_fields.keys()]
# [print(nearby_ticket) for nearby_ticket in nearby_tickets]


print(f"starting with {len(nearby_tickets)} tickets + 1 (our own ticket)")

valid_tickets = []
invalid_tickets = []

rules = parsed_fields.keys()
#
first_lower_bound = 100000
second_lower_bound = 100000
first_upper_bound = 0
second_upper_bound = 0

# Assume that we can flatten all bounds into 1 set of rules, rather than check each ticket against N sets of rules
for key in rules:
    rule = parsed_fields[key]
    if rule[0] < first_lower_bound:
        first_lower_bound = rule[0]

    if rule[1] > first_upper_bound:
        first_upper_bound = rule[1]

    if rule[2] < second_lower_bound:
        second_lower_bound = rule[2]

    if rule[3] > second_upper_bound:
        second_upper_bound = rule[3]

flat_rules = [first_lower_bound, first_upper_bound, second_lower_bound, second_upper_bound]

# print(f"first_lower_bound: {first_lower_bound} - first_upper_bound: {first_upper_bound} - second_lower_bound: "
#       f"{second_lower_bound} - second_upper_bound: {second_upper_bound}")

for ticket in nearby_tickets:
    invalid = False
    # print(f"ticket: {ticket}")
    for field in ticket:
        found = False
        # print(f"field: {field}")
        for rule in rules:
            rule_arr = parsed_fields[rule]
        # if (first_lower_bound <= field <= first_upper_bound) or (second_lower_bound <= field <= second_upper_bound):
        #     # valid_tickets += ticket
        #     print(f"FOUND - field: {field} - rules: {rules}")
        #     found = True
        #     break

            if (rule_arr[0] <= field <= rule_arr[1]) or (rule_arr[2] <= field <= rule_arr[3]):
                # valid_tickets += ticket
                # print(f"FOUND - field: {field} - rule: {rule} - rule_arr: {rule_arr}")
                found = True
                break

        if not found:
            # print(f"INVALID Field: {field}")
            invalid = True
            break

    if invalid:
        invalid_tickets += [ticket]
    else:
        valid_tickets += [ticket]

    # break


# print(flat_rules)
print(f"valid_tickets: {len(valid_tickets)}")
print(f"invalid_tickets: {len(invalid_tickets)}")
print(f"num rules: {len(rules)}")

field_index = 0
rule_index = 0
ordered_fields = [None for x in range(len(rules))]

for rule in rules:
    field_index = 0
    rule_arr = parsed_fields[rule]
    print(f"rule: {rule} - rule_arr: {rule_arr}")
    while True:
        invalid = False
        # print(f"field_index: {field_index}")
        for valid_ticket in valid_tickets:

            field = valid_ticket[field_index]
            # print(f"field: {field}")
            if (rule_arr[0] <= field <= rule_arr[1]) or (rule_arr[2] <= field <= rule_arr[3]):
                # print(f"field: {field} - works!")
                continue
            else:
                # print(f"field: {field} - doesn't work!")
                invalid = True
                break

        if invalid:
            field_index += 1
        else:
            ordered_fields[field_index] = rule
            print(ordered_fields)
            break
    # break

print(ordered_fields)

    # while len(ordered_fields) < len(parsed_fields):
#     for rule in rules:
#         invalid = False
#         rule_arr = parsed_fields[rule]
#         for valid_ticket in valid_tickets:
#
#             field = valid_ticket[field_index]
#             if (rule_arr[0] <= field <= rule_arr[1]) or (rule_arr[2] <= field <= rule_arr[3]):
#                 continue
#             else:
#                 invalid = True
#                 break
#
#         if invalid:
#             field_index += 1
#         else:


