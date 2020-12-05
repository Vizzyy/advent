import math

with open('./input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# print(sanitized_inputs)

# 0 - 15
# 0 - 7     F
# 4 - 7     B
# 4 - 5     F
# 5         B


def get_seat_id(bsp):

    row = bsp[:-3]
    row_min = 0
    row_max = 127

    col_min = 0
    col_max = 7
    column = bsp[-3:]

    # print(f"min: {row_min}, max: {row_max}")
    for letter in row:
        if letter == "F":
            combined = row_min + row_max
            diff = math.floor(combined/2)
            # print(diff)
            row_max = diff
        if letter == "B":
            combined = row_min + row_max
            diff = math.ceil(combined/2)
            # print(diff)
            row_min = diff
        # print(f"{letter} - min: {row_min}, max: {row_max}")

    for letter in column:
        if letter == "L":
            combined = col_min + col_max
            diff = math.floor(combined/2)
            # print(diff)
            col_max = diff
        if letter == "R":
            combined = col_min + col_max
            diff = math.ceil(combined/2)
            # print(diff)
            col_min = diff
        # print(f"{letter} - min: {col_min}, max: {col_max}")

    return row_min, col_min


highest = 0
highest_ticket = ""

for ticket in sanitized_inputs:
    id = get_seat_id(ticket)
    total = id[0] * 8 + id[1]
    if total > highest:
        highest = total
        highest_ticket = ticket

print(highest_ticket)
print(highest)

seat_map = [x for x in range(1000)]

for ticket in sanitized_inputs:
    id = get_seat_id(ticket)
    total = id[0] * 8 + id[1]
    seat_map[total] = 1

[print(x) for x in seat_map if x != 1]


