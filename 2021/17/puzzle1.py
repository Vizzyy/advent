start_pos = [0, 0]
start_vector = [6, 9]
steps_limit = 1000
scalar_limit = 200


with open('input2.txt', 'r') as file:
    text = file.read().strip().replace(',', '').split(' ')
    x_area = text[2].split('=')[1].split('..')
    y_area = text[3].split('=')[1].split('..')
    target_area = [
        [int(x_area[0]), int(y_area[0])],  # bottom left
        [int(x_area[0]), int(y_area[1])],  # top left
        [int(x_area[1]), int(y_area[0])],  # bottom right
        [int(x_area[1]), int(y_area[1])],  # top right
    ]

print(f'target_area: {target_area}')


def is_within_target(position) -> bool:
    global target_area
    pos_x = position[0]
    pos_y = position[1]

    if target_area[0][0] <= pos_x <= target_area[3][0] and target_area[0][1] <= pos_y <= target_area[3][1]:
        return True
    else:
        return False


def trajectory_decay(vector: list):
    x_vector = vector[0]
    y_vector = vector[1]

    if x_vector > 0:
        result_x = x_vector - 1
    elif x_vector < 0:
        result_x = x_vector + 1
    else:
        result_x = 0

    result_y = y_vector - 1

    return [result_x, result_y]


def do_trajectory(initial_vector):
    current_pos = [0, 0]
    current_vector = initial_vector
    highest_point = 0

    # print(f'starting at: {current_pos}, with vector: {current_vector}')

    for i in range(1, steps_limit):
        current_pos = [current_pos[0] + current_vector[0], current_pos[1] + current_vector[1]]
        current_vector = trajectory_decay(current_vector)
        in_target = is_within_target(current_pos)
        if current_pos[1] > highest_point:
            highest_point = current_pos[1]
        # print(f'step {i}: current_pos: {current_pos}, current_vector: {current_vector}, '
        #       f'highest_point: {highest_point}, in_target: {in_target}')
        if in_target:
            print(f'step {i}: current_pos: {current_pos}, initial_vector: {initial_vector}, '
                  f'highest_point: {highest_point}, current_vector: {current_vector}')
            return highest_point
        if current_vector[0] == 0 and current_pos[1] < target_area[0][1]:
            # print('We have drifted below the target!')
            return 0


max_height = 0
for x in range(scalar_limit):
    for y in range(scalar_limit):
        # print(f'Simulating start_vector: {[x, y]}')
        output_height = do_trajectory([x, y])
        if output_height > max_height:
            max_height = output_height

print(f'max_height: {max_height}')
