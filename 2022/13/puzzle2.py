import datetime
import ast
import functools

start = datetime.datetime.now()

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [line.strip().split('\n') for line in inputs.strip().split('\n\n')]
inputs = [[ast.literal_eval(pair) for pair in line] for line in inputs]

def is_in_right_order(left_input, right_input):
    print(f'[is_in_right_order] - left: {left_input} - right: {right_input}')

    for idx in range(max(len(left_input), len(right_input))):

        try:
            inner_left = left_input.copy()[idx]
        except IndexError:
            print(f'Left list runs out of items first -- ordered True!')
            return True
            
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

        # integer comparison. return if right is lower (out of order)
        elif inner_right < inner_left:
            print(f'right is lower (out of order): {inner_right < inner_left}')
            return False

        # finally, as soon as we encounter a pairing that is not equal, and is properly ordered, return true
        if inner_right != inner_left:
            print(f'Correct Order! Left is less than right.')
            return True

    print(f'Top level return True')
    return True


full_packets = []
for left, right in inputs:
    full_packets.append(left.copy())
    full_packets.append(right.copy())

full_packets.append([[2]])
full_packets.append([[6]])


def compare(a, b):
    if is_in_right_order(a.copy(), b.copy()):
        return 1
    else:
        return -1


compare_key = functools.cmp_to_key(compare)
sorted_packets = sorted(full_packets, key=compare_key, reverse=True)

# print()
# [print(line) for line in full_packets]
print()
[print(line) for line in sorted_packets]

packet_1 = sorted_packets.index([[6]]) + 1
packet_2 = sorted_packets.index([[2]]) + 1

print(f'\n{packet_1 * packet_2}')

print(f'elapsed: {datetime.datetime.now() - start}')
