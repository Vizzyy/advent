with open('input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# print(sanitized_inputs)

# print(len(sanitized_inputs[0]))

trees = 0
position = 0

for row in sanitized_inputs:
    item = row[position % 31]
    if item == "#":
        trees += 1
    position += 3

# print(trees)


def route(right, down):

    print(f"right: {right} - down: {down}")
    trees = 0
    position = 0
    down_bool = False

    for row in range(len(sanitized_inputs)):
        if down_bool and down > 1:
            down_bool = False
            continue
        else:
            down_bool = True
        # print(row)
        temp_row = sanitized_inputs[row]
        item = temp_row[position % 31]
        # print(item)
        if item == "#":
            trees += 1
        position += right

    print(trees)
    return trees


# print(route(1, 1))
# print(route(3, 1))
# print(route(5, 1))
# print(route(7, 1))
# print(route(1, 2))

print(route(1, 1) * route(3, 1) * route(5, 1) * route(7, 1) * route(1, 2))
