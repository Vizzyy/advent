import datetime

with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')[1:]

start = datetime.datetime.now()

# we keep a pointer, our current location
pointer = "/"
# we initialize a filesystem. it's easier to flatten the entire file system instead of nesting everything
filesystem = {
    "/": {
        'contents': [],
        'size': 0
    }
}

# for every line of input
for line in inputs:
    # if it is not a command, then we need to add it to our file system
    if '$' not in line:
        first, second = line.split(' ')
        # a new directory is a new key in our filesystem, with the dir name appended to our pointer
        if first == 'dir':
            filesystem[f'{pointer}{second}/'] = {
                'contents': [],
                'size': 0
            }
        # a new file is instead appended to the current "pointer" directories "contents"
        # instead of complicating things further with a "file" struct, we just name the file the size it has
        else:
            filesystem[f'{pointer}']['contents'].append(int(first))
    # for changing directories in either direction, we simply modify the pointer to add or remove layers
    elif "$ cd" in line:
        if '..' in line:
            pointer = '/'.join(pointer.split('/')[:-2]) + '/'
        else:
            pointer += f'{line.split("$ cd ")[1]}/'

# once we have all of our directories initialized, we sort them by the length of the "path" to that directory.
# so the deepest directory is first and the root is last. (reversed)
sorted_keys = sorted(list(filesystem.keys()), key=len, reverse=True)
# iterating over the list of directories we sum the size of the files in the directory
for directory in range(len(sorted_keys)):
    dir_key = sorted_keys[directory]
    dir_size = sum(filesystem[dir_key]["contents"])
    filesystem[dir_key]["size"] += dir_size

# then we do some more preprocessing, where we create a map of directories by depth. where depth for /a/b/c/ == 3
dirs_by_depth = {}
for key in sorted_keys:
    depth = len(key.split('/')) - 2
    if depth not in dirs_by_depth.keys():
        dirs_by_depth[depth] = [key]
    else:
        dirs_by_depth[depth].append(key)

# starting with the deepest directories we check whether it is a child to any directory above it,
# and if so we add the sum of the child's directory to the sum of the parent's directory
for depth in sorted(list(dirs_by_depth.keys()), reverse=True):
    if depth == 0:
        break
    for path in dirs_by_depth[depth]:
        for parent_path in dirs_by_depth[depth - 1]:
            if path.startswith(parent_path):
                filesystem[parent_path]['size'] += filesystem[path]['size']


# current_usage is just the root directory's size
current_usage = filesystem[sorted_keys[-1]]["size"]
print(f'\ncurrent_usage: {current_usage}')
current_free = 70000000 - current_usage
print(f'current_free: {current_free}')

# and then for all the potential subdirectories that we could delete to reach the target size, we add it to our list
possibilities = []
for key in sorted_keys:
    if filesystem[key]['size'] + current_free >= 30000000:
        possibilities.append(filesystem[key]['size'])

# and return the first (smallest) in the list
possibilities.sort()
print(f'answer: {possibilities[0]}')
print(f'elapsed: {datetime.datetime.now() - start}')
