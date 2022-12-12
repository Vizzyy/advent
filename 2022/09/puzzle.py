import math

with open('input.txt', 'r') as file:
    inputs = file.read()
directions = [direction.split(' ') for direction in inputs.strip().split('\n')]

head = [0, 0]
tail = [0, 0]

head_positions = [[0, 0]]
tail_positions = [[0, 0]]

# test_grid = [['  ' for x in range(6)] for y in range(5)]
# test_grid2 = [['  ' for x in range(6)] for y in range(5)]


def handle_tail():
    global tail, head, tail_positions
    distance = math.dist(head, tail)
    # print(f'head: {head}, tail: {tail}, distance: {distance}')
    if distance >= 2:
        v4x = math.ceil((head[0] - tail[0]) / round(distance)) if head[0] - tail[0] > 0 else math.floor((head[0] - tail[0]) / round(distance))
        v4y = math.ceil((head[1] - tail[1]) / round(distance)) if head[1] - tail[1] > 0 else math.floor((head[1] - tail[1]) / round(distance))
        vector4 = [v4x, v4y]
        # print(f'{tail[0] + vector4[0]}, {tail[1] + vector4[1]}')
        tail = [tail[0] + vector4[0], tail[1] + vector4[1]]
        # print(f'vector: {vector}, v2: {vector2}, v3: {vector3}, v4: {vector4}, new tail: {tail}')
        # print(f'vector: {vector4}, new tail: {tail}')
        tail_positions.append(tail.copy())


def handle_instruction(direction):
    for i in range(int(direction[1])):
        if direction[0] == 'R':
            head[0] += 1
        if direction[0] == 'L':
            head[0] -= 1
        if direction[0] == 'U':
            head[1] += 1
        if direction[0] == 'D':
            head[1] -= 1
        head_positions.append(head.copy())
        handle_tail()


for direction in directions:
    # print(direction)
    handle_instruction(direction)

# print(head_positions)
# print(tail_positions)
#
# for tail_pos in tail_positions[::-1]:
#     test_grid[tail_pos[1]][tail_pos[0]] = f'{tail_positions.index(tail_pos):02}'
# for head_pos in head_positions:
#     test_grid2[head_pos[1]][head_pos[0]] = f'{head_positions.index(head_pos):02}'
#
# [print(line) for line in test_grid2[::-1]]
# print()
# [print(line) for line in test_grid[::-1]]

print(len([list(x) for x in set(tuple(x) for x in tail_positions)]))
