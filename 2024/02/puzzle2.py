import copy

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

# print(inputs)

inputs = [[int(part) for part in level.split()] for level in inputs]

[print(input) for input in inputs]
print()


def get_deltas_from_level(level):
    deltas = []
    
    for idx in range(len(level)):
        if idx < len(level)-1:
            deltas.append(level[idx] - level[idx+1])

    return deltas


def is_level_safe(level, deep=True):
    deltas = get_deltas_from_level(level)
    print(f'deltas from {level}: {deltas}')

    num_increasing_safe = sum(1 for delta in deltas if 3 >= delta > 0)
    num_decreasing_safe = sum(1 for delta in deltas if -3 <= delta < 0)

    if num_increasing_safe == len(level)-1: # if all values were safe increase
        print(f'num_increasing_safe!')
        return True
    
    if num_decreasing_safe == len(level)-1: # if all values were safe decrease
        print(f'num_decreasing_safe!')
        return True

    if deep:   
        for idx in range(len(level)):
            inner_copy = copy.copy(level)
            inner_copy.pop(idx)
            if is_level_safe(inner_copy, False):
                return True

    print(f'deep: {deep}, not safe!')
    return False


count_safe = 0
for level in inputs:
    if is_level_safe(level): 
        count_safe += 1

print(count_safe)