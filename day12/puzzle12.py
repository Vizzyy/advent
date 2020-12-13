from copy import copy

with open('./input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
print(sanitized_inputs)
print()

directions = ["E", "S", "W", "N"]  # Starting East, clockwise

facing = directions[0]
position_x = 0
position_y = 0


def directions_generator():
    print(f"Routes: {directions}")
    while True:
        for direction in directions:
            yield direction


def parse_translation(distance, direction = None):
    global position_x
    global position_y
    global facing

    if direction is None:
        switch = facing
    else:
        switch = direction

    if switch == "E":
        position_x += int(distance)
    if switch == "W":
        position_x -= int(distance)
    if switch == "N":
        position_y += int(distance)
    if switch == "S":
        position_y -= int(distance)


def parse_rotation(letter, degree):
    global facing
    turns = int(degree) / 90
    if letter == "L":
        turns = len(directions) - turns  # generator can only move next, not prev
    directions_iterator = directions_generator()
    curr_dir = next(directions_iterator)
    while curr_dir != facing:
        curr_dir = next(directions_iterator)

    print(f"facing: {facing} - curr_dir: {curr_dir} - turns {turns}")
    for i in range(int(turns)):
        curr_dir = next(directions_iterator)
    print(f"facing: {facing} - curr_dir: {curr_dir}")
    facing = curr_dir


for instruction in sanitized_inputs:
    letter = instruction[0]
    print(letter)
    if letter == "F":
        parse_translation(instruction[1:])
    if letter == "L" or letter == "R":
        parse_rotation(letter, instruction[1:])
    if letter == "N" or letter == "S" or letter == "E" or letter == "W":
        parse_translation(instruction[1:], letter)

print("\nSolution:")
print(f"facing: {facing} - position_x: {position_x} - position_y {position_y}")
print(f"Manhattan Distance: {abs(position_x) + abs(position_y)}")
