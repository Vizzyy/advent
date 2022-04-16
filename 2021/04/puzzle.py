with open('input.txt', 'r') as file:
    numbers_drawn = file.readline()
    inputs = file.read()

numbers_drawn = [int(number) for number in numbers_drawn.split(',')]

bingo_boards = [[row.strip().split() for row in board.strip().split('\n')] for board in inputs.split('\n\n')]
bingo_boards = [[[int(digit) for digit in row] for row in board] for board in bingo_boards]

winning_board = None
numbers_drawn_so_far = []


def is_winning_combo(numbers_drawn_so_far, combo):
    for number in combo:
        if number in numbers_drawn_so_far:
            continue
        else:
            return False
    return True


for number_drawn in numbers_drawn:
    last_number_drawn = number_drawn
    numbers_drawn_so_far.append(number_drawn)
    for bingo_board in bingo_boards:
        columns = [[int(t_row[idx]) for t_row in bingo_board] for idx in range(5)]
        possible_combos = bingo_board + columns  # all rows + columns
        for combo in possible_combos:
            if is_winning_combo(numbers_drawn_so_far, combo):
                winning_board = bingo_board
                break

        if winning_board:
            break

    if winning_board:
        break

print(f"winning_board: {winning_board}")
print(f"numbers_drawn_so_far: {numbers_drawn_so_far}")

unmarked_nums = []

for row in winning_board:
    for digit in row:
        if digit not in numbers_drawn_so_far:
            unmarked_nums.append(digit)

print(f"unmarked_nums: {unmarked_nums}")
print(sum(unmarked_nums) * last_number_drawn)
