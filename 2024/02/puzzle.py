with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')

# print(inputs)

inputs = [[int(part) for part in level.split()] for level in inputs]

# [print(input) for input in inputs]


safe_count = 0
for level in inputs:
    # print(level)
    was_safe = True
    
    if level[0] > level[1]:
        ordering = 1
    elif level[0] == level[1]:
        continue
    else:
        ordering = -1 # -1 represents increasing values [1,3,5,..] (1 - 3 = -2)

    for idx in range(len(level)):

        if idx < len(level)-1:
            # print(f'level[idx]:{level[idx]}, level[idx+1]: {level[idx+1]}')
            if 3 >= (ordering * (level[idx] - level[idx+1])) >= 1:
                # safe
                continue
            else:
                # print('not safe!')
                was_safe = False
                break
    if was_safe:
        # print('safe!')
        safe_count += 1

print(safe_count)