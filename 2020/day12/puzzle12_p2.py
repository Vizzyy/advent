import math

with open('input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
# print(sanitized_inputs)
# print()

position_x = 0
position_y = 0
waypoint_x = 10
waypoint_y = 1


# rotating a 2d vector counterclockwise around origin
# x2 = cos@x1 - sin@y1
# y2 = sin@x1 + cos@y1
# where @ = angle in [90,180,270]
def rotate_waypoint(letter, angle):
    global waypoint_x
    global waypoint_y

    cosine = math.cos(math.radians(int(angle)))
    sine = math.sin(math.radians(int(angle)))

    if letter == "R":
        new_x = int(cosine * waypoint_x) + int(sine * waypoint_y)
        new_y = -1 * int(sine * waypoint_x) + int(cosine * waypoint_y)
    if letter == "L":
        new_x = int(cosine * waypoint_x) - int(sine * waypoint_y)
        new_y = int(sine * waypoint_x) + int(cosine * waypoint_y)

    # print(f"rotation({letter}{angle}) - old ({waypoint_x}, {waypoint_y}) - ({new_x}, {new_y})")

    waypoint_x = new_x
    waypoint_y = new_y


def waypoint_translation(letter, distance):
    global waypoint_x
    global waypoint_y

    if letter == "E":
        waypoint_x += int(distance)
    if letter == "W":
        waypoint_x -= int(distance)
    if letter == "N":
        waypoint_y += int(distance)
    if letter == "S":
        waypoint_y -= int(distance)


def move_ship(multiplier):
    global position_x
    global position_y
    global waypoint_x
    global waypoint_y

    position_x = position_x + (waypoint_x * int(multiplier))
    position_y = position_y + (waypoint_y * int(multiplier))


for instruction in sanitized_inputs:
    # print(f"instruction: {instruction} - waypoint ({waypoint_x}, {waypoint_y}) - position ({position_x}, {position_y}) ")
    letter = instruction[0]
    # print(letter)
    if letter == "F":
        move_ship(instruction[1:])
    if letter == "L" or letter == "R":
        rotate_waypoint(letter, instruction[1:])
    if letter == "N" or letter == "S" or letter == "E" or letter == "W":
        waypoint_translation(letter, instruction[1:])
    # print(f"AFTER: waypoint ({waypoint_x}, {waypoint_y}) - position ({position_x}, {position_y}) ")

print("\nSolution:")
print(f"position_x: {waypoint_x} - position_y {waypoint_y} - position_x: {position_x} - position_y {position_y}")
print(f"Manhattan Distance: {abs(position_x) + abs(position_y)}")
