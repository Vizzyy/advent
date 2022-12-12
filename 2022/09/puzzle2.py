import math

with open('input.txt', 'r') as file:
    inputs = file.read()
directions = [direction.split(' ') for direction in inputs.strip().split('\n')]

# current positions
head = [0, 0]
tail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

# cumulative positions
head_positions = [[0, 0]]
tail_positions = [[0, 0]]

# Uncomment for visualization
# x_offset = 11
# y_offset = 5
# x_max = 15 + x_offset
# y_max = 16 + y_offset
# test_grid = [['.' for x in range(x_max)] for y in range(y_max)]


# take in two relative nodes, and return the new position of tail
def handle_tail(head_node, tail_node):
    global tail_positions
    # calculate distance between two points
    distance = math.dist(head_node, tail_node)
    if distance >= 2:
        # calculate the normalized vector, by calculating the distance between Xs and Ys, and dividing by the distance
        # we have to be careful about floor and ceil, because ceil works oppositely with negative numbers
        vx = math.ceil((head_node[0] - tail_node[0]) / round(distance)) if head_node[0] - tail_node[0] > 0 else math.floor((head_node[0] - tail_node[0]) / round(distance))
        vy = math.ceil((head_node[1] - tail_node[1]) / round(distance)) if head_node[1] - tail_node[1] > 0 else math.floor((head_node[1] - tail_node[1]) / round(distance))
        vector = [vx, vy]
        # add our normalized vector to the old tail to get new tail
        new_tail = [tail_node[0] + vector[0], tail_node[1] + vector[1]]
        return new_tail
    else:
        return tail_node.copy()


def handle_instruction(direction):
    global tail_positions, tail, head
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

        # iterate through all the tail nodes
        head_node = head.copy()
        for tail_node_idx in range(len(tail)):
            # update the position of the tail node given the node in front of it
            tail[tail_node_idx] = handle_tail(head_node, tail[tail_node_idx])
            # only update the cumulative tail positions if it is the true tail
            if tail_node_idx == len(tail) - 1:
                tail_positions.append(tail[tail_node_idx].copy())
            head_node = tail[tail_node_idx].copy()


for direction in directions:
    # Uncomment for visualization
    # if directions.index(direction) > 4:
    #     break

    handle_instruction(direction)


# Uncomment for visualization
# for tail_pos in tail:
#     test_grid[tail_pos[1]+y_offset][tail_pos[0]+x_offset] = f'{tail.index(tail_pos) + 1}'
# test_grid[head[1]+y_offset][head[0]+x_offset] = 'H'
# test_grid[0+y_offset][0+x_offset] = 's'
#
# [print(line) for line in test_grid[::-1]]


print()
print(len([list(x) for x in set(tuple(x) for x in tail_positions)]))
