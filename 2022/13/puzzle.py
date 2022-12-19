import datetime
import ast

start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [line.strip().split('\n') for line in inputs.strip().split('\n\n')]
# [print(line) for line in inputs]
inputs = [[ast.literal_eval(pair) for pair in line] for line in inputs]
# [print(line) for line in inputs]


def is_in_right_order(left_input, right_input):
    print(f'[is_in_right_order] - left: {left_input} - right: {right_input}')

    for idx in range(max(len(left_input), len(right_input))):
        try:
            inner_left = left_input.copy()[idx]
        except IndexError:
            print(f'Left list runs out of items first -- ordered True!')
            return True
            # continue
        try:
            inner_right = right_input.copy()[idx]
        except IndexError:
            print(f'Right list runs out of items first -- ordered False!')
            return False
        print(f'[inner-loop] - left: {inner_left} (list={isinstance(inner_left, list)}), '
              f'right: {inner_right} (list={isinstance(inner_right, list)})')

        # if comparing different types, promote to list
        if isinstance(inner_left, list) and not isinstance(inner_right, list):
            print(f'promoting right to list')
            inner_right = [inner_right]
        if isinstance(inner_right, list) and not isinstance(inner_left, list):
            print(f'promoting left to list')
            inner_left = [inner_left]

        # if comparing two lists, recurse into the nested list
        if isinstance(inner_left, list) and isinstance(inner_right, list):
            print('recursing nested list')
            if not is_in_right_order(inner_left.copy(), inner_right.copy()):
                print(f'Returning False because recursive call returned False')
                return False
            else:
                print(f'[after recursion] - inner_left: {inner_left}, inner_right {inner_right}')
                continue

        # integer comparison. return if right is lower (out of order)
        if inner_right < inner_left:
            print(f'right is lower (out of order): {inner_right < inner_left}')
            return False

        # finally, as soon as we encounter a pairing that is not equal, and is properly ordered, return true
        if inner_right != inner_left:
            print(f'Correct Order! {inner_right != inner_left}')
            return True
            # continue

    print(f'Top level return True')
    return True


packet_index = 1
correct_packets = []
for left, right in inputs:
    print(f'== Pair {packet_index} ==')
    correct = is_in_right_order(left, right)
    if correct:
        correct_packets.append(packet_index)
    packet_index += 1
    print(f'[main] - {correct}\n')

print(correct_packets)
print(sum(correct_packets))

print(f'elapsed: {datetime.datetime.now() - start}')
