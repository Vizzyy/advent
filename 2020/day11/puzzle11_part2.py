from copy import copy

with open('input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = [letter for letter in num.replace("\n", "").replace("L", "#")]
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
# print()
row_len = len(sanitized_inputs[0])
col_len = len(sanitized_inputs)
print(f"row_len: {row_len} - col_len: {col_len}")


def occupied_adjacents(x, y, state):
    # print(f"incoming loc: {x}, {y}")
    adj_occupied = 0
    adj_empty = 0
    adjacent_seats = [(x - 1, y - 1),
                      (x, y - 1),
                      (x + 1, y - 1),
                      (x - 1, y),
                      (x + 1, y),
                      (x - 1, y + 1),
                      (x, y + 1),
                      (x + 1, y + 1)]

    top_left = "."
    start_x = x-1
    start_y = y-1
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            top_left = spot
            adjacent_seats[0] = (start_x, start_y)
            break
        else:
            start_x -= 1
            start_y -= 1

    top_middle = "."
    start_x = x
    start_y = y-1
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            top_middle = spot
            adjacent_seats[1] = (start_x, start_y)
            break
        else:
            start_y -= 1

    top_right = "."
    start_x = x+1
    start_y = y-1
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            top_right = spot
            adjacent_seats[2] = (start_x, start_y)
            break
        else:
            start_x += 1
            start_y -= 1

    left = "."
    start_x = x-1
    start_y = y
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            left = spot
            adjacent_seats[3] = (start_x, start_y)
            break
        else:
            start_x -= 1

    right = "."
    start_x = x+1
    start_y = y
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            right = spot
            adjacent_seats[4] = (start_x, start_y)
            break
        else:
            start_x += 1

    bottom_left = "."
    start_x = x-1
    start_y = y+1
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            bottom_left = spot
            adjacent_seats[5] = (start_x, start_y)
            break
        else:
            start_x -= 1
            start_y += 1

    bottom = "."
    start_x = x
    start_y = y+1
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            bottom = spot
            adjacent_seats[6] = (start_x, start_y)
            break
        else:
            start_y += 1

    bottom_right = "."
    start_x = x+1
    start_y = y+1
    while True:
        if start_x >= row_len or start_x < 0 or start_y >= col_len or start_y < 0:
            break
        row = state[start_y]
        spot = row[start_x]
        if spot == "#" or spot == "L":
            bottom_right = spot
            adjacent_seats[7] = (start_x, start_y)
            break
        else:
            start_x += 1
            start_y += 1

    # print(adjacent_seats)
    for seat in adjacent_seats:
        # print(f"seat: {seat}")
        if 0 <= seat[0] < row_len and 0 <= seat[1] < col_len:
            row = state[seat[1]]
            # print(row)
            # print(f"row: {row} - seat: {seat}")
            spot = row[seat[0]]
            # print(f"spot: {spot}, seat: {seat}")
            if spot == "#":
                # print(f"row: {''.join(row)} - spot: {spot}, seat: {seat}")
                adj_occupied += 1
            elif spot == 'L' or spot == '.':
                adj_empty += 1
        else:
            adj_empty += 1
    # print(f"x: {x}, y: {y}, adj count: {adj_occupied}")
    return adj_occupied, adj_empty


translations = 0

new_state = copy(sanitized_inputs)
[print(''.join(x)) for x in new_state]
print()


break_pt = 1
while True:
    temp_state = copy(new_state)  # the one we alter per loop of While
    # [print(''.join(x)) for x in temp_state]
    # print()
    for y in range(len(new_state)):
        row = new_state[y]
        new_row = copy(row)
        for x in range(len(row)):
            seat = new_row[x]
            if new_row[x] == '.':
                continue

            adj_state = occupied_adjacents(x, y, new_state)
            if new_row[x] == "#" and adj_state[0] >= 5:
                # new_row = copy(row)
                new_row[x] = "L"
                temp_state[y] = new_row
                # print(''.join(new_row))
                # new_state[y] = new_row
                # print(f"old: {row} - new {new_state[y]}")
                translations += 1
            elif new_row[x] == "L" and adj_state[1] == 8:
                new_row[x] = "#"
                temp_state[y] = new_row
                # print(''.join(new_row))
                translations += 1
        # break

    if translations == 0:# or break_pt > 1:
        break
    else:
        new_state = copy(temp_state)
        print(f"translations: {translations}")
        [print(''.join(x)) for x in new_state]
        print()
        translations = 0
        break_pt += 1


print()
print("Finished State:")
# [print(''.join(x)) for x in temp_state]

one_dimensional = ''.join(str(item) for innerlist in temp_state for item in innerlist)
print(f"Occupied Seats: {one_dimensional.count('#')}")
