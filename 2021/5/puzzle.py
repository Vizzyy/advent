with open('input.txt', 'r') as file:
    numbers_drawn = file.readlines()

numbers_drawn = [[[int(number) for number in coord.split(',')] for coord in line.strip().split(' -> ')] for line in numbers_drawn]
# grid = [[0 for column in range(len(numbers_drawn))] for row in range(len(numbers_drawn))]
grid = [[0 for column in range(1000)] for row in range(1000)]

# [print(row) for row in grid]
# [print(vector) for vector in numbers_drawn]

for vector in numbers_drawn:
    coords_in_vector = []
    start_coord = vector[0]
    end_coord = vector[1]

    # ignore diagonal lines
    if start_coord[0] != end_coord[0] and start_coord[1] != end_coord[1]:
        print(f"skipping diagonal: {vector}")
        print()
        continue

    delta = [end_coord[0] - start_coord[0], end_coord[1] - start_coord[1]]
    print(vector)
    print(delta)

    x_direction = 1 if delta[0] >= 0 else -1
    y_direction = 1 if delta[1] >= 0 else -1

    for x in range(abs(delta[0])):
        coords_in_vector.append([start_coord[0] + x * x_direction, start_coord[1]])
    for y in range(abs(delta[1])):
        coords_in_vector.append([start_coord[0], start_coord[1] + y * y_direction])

    coords_in_vector.append(end_coord)

    print(coords_in_vector)

    for coord_in_vector in coords_in_vector:
        grid_loc_value = grid[coord_in_vector[1]][coord_in_vector[0]]
        grid[coord_in_vector[1]][coord_in_vector[0]] = grid_loc_value + 1

    print()

[print(row) for row in grid]

count_at_least_two_overlap = 0

for y in grid:
    for x in y:
        if x >= 2:
            count_at_least_two_overlap += 1

print(count_at_least_two_overlap)
