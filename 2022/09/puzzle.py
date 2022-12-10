with open('test.txt', 'r') as file:
    inputs = file.read()
directions = [direction.split(' ') for direction in inputs.strip().split('\n')]

head = [0, 0]
tail = [0, 0]

head_positions = [[0,0]]
tail_positions = [[0,0]]


def handle_tail(previous_head, current_head):
    new_tail = []

    

    return new_tail


def handle_direction(direction):
    previous_head = head.copy()
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
        tail_positions.append(handle_tail(previous_head, head.copy()))
        

for direction in directions:
    print(direction)
    handle_direction(direction)
    
print(head_positions)