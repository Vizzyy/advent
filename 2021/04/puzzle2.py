with open('input.txt', 'r') as file:
    numbers_drawn = file.readline()
    inputs = file.read()

numbers_drawn = [int(number) for number in numbers_drawn.split(',')]
print(numbers_drawn)
bingo_boards = [[row.strip().split() for row in board.strip().split('\n')] for board in inputs.split('\n\n')]
bingo_boards = [[[int(digit) for digit in row] for row in board] for board in bingo_boards]

winning_boards = []
numbers_drawn_so_far = []
print(f"num boards: {len(bingo_boards)}")


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
    for bingo_board_idx in range(len(bingo_boards)):
        bingo_board = bingo_boards[bingo_board_idx]
        columns = [[int(t_row[idx]) for t_row in bingo_board] for idx in range(5)]
        possible_combos = bingo_board + columns  # all rows + columns
        for combo in possible_combos:
            if is_winning_combo(numbers_drawn_so_far, combo):
                print(f"winning board: {bingo_boards[bingo_board_idx]}")
                winning_boards.append(bingo_boards[bingo_board_idx])
                break

    for winning_board in winning_boards:
        try:
            bingo_boards.pop(bingo_boards.index(winning_board))
        except Exception as e:
            pass

    print(f"winning_boards: {len(winning_boards)}, remaining boards: {len(bingo_boards)}, last_number_drawn: {last_number_drawn}")
    if len(bingo_boards) == 0:
        break

unmarked_nums = []
losing_board = winning_boards[len(winning_boards) - 1]
print()
print(f"losing_board: {losing_board}")

for row in losing_board:
    for digit in row:
        if digit not in numbers_drawn_so_far:
            unmarked_nums.append(digit)

print(f"unmarked_nums: {unmarked_nums}")
print(sum(unmarked_nums) * last_number_drawn)
