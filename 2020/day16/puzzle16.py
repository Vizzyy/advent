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
    parsed_fields[line[0]] = line[1].split(' or ')

all_field_rules = []

for key in parsed_fields.keys():
    all_field_rules += parsed_fields[key]


total_error = 0

all_ticket_fields = []

for ticket in nearby_tickets:
    all_ticket_fields += ticket


for field in all_ticket_fields:
    found = False
    for rule in all_field_rules:
        rule_parsed = rule.split('-')
        if int(rule_parsed[0]) <= field <= int(rule_parsed[1]):
            found = True
            break
    if not found:
        total_error += field

print(total_error)
