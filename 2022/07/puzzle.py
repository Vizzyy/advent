with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')[1:]

print(inputs)

pointer = "/"
filesystem = {
    "/": {
        'contents': [],
        'size': 0
    }
}

for line in inputs:
    print(f'line: {line}, pointer: {pointer}')
    if '$' not in line:
        first, second = line.split(' ')
        if first == 'dir':
            filesystem[f'{pointer}{second}/'] = {
                'contents': [],
                'size': 0
            }
        else:
            filesystem[f'{pointer}']['contents'].append(int(first))
    elif "$ cd" in line:
        if '..' in line:
            pointer = '/'.join(pointer.split('/')[:-2]) + '/'
        else:
            pointer += f'{line.split("$ cd ")[1]}/'
        print(f'pointer: {pointer}')

print()
sorted_keys = sorted(list(filesystem.keys()), key=len, reverse=True)
for directory in range(len(sorted_keys)):
    dir_key = sorted_keys[directory]
    dir_size = sum(filesystem[dir_key]["contents"])
    filesystem[dir_key]["size"] += dir_size
    print(f'dir_key: "{dir_key}" - dir_size: {dir_size}')

print()
dirs_by_depth = {}
for key in sorted_keys:
    depth = len(key.split('/')) - 2
    # print(f'key: {key} - depth: {depth}')
    if depth not in dirs_by_depth.keys():
        dirs_by_depth[depth] = [key]
    else:
        dirs_by_depth[depth].append(key)

# print(dirs_by_depth)

for depth in sorted(list(dirs_by_depth.keys()), reverse=True):
    if depth == 0:
        break
    for path in dirs_by_depth[depth]:
        for parent_path in dirs_by_depth[depth - 1]:
            if path.startswith(parent_path):
                filesystem[parent_path]['size'] += filesystem[path]['size']


[print(f'{key} - {filesystem[key]["size"]}') for key in sorted_keys]

target_dirs = []
for key in sorted_keys:
    if filesystem[key]["size"] <= 100000:
        target_dirs.append(filesystem[key]["size"])
print(f'\nsum: {sum(target_dirs)}')
