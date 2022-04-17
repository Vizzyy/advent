with open('input.txt') as file:
    caves = file.read().strip().split('\n')

cave_map = {}

for path in caves:
    # forwards
    path_pair = path.split('-')
    if path_pair[0] in cave_map.keys():
        cave_map[path_pair[0]].append(path_pair[1])
    else:
        cave_map[path_pair[0]] = [path_pair[1]]

    # backwards
    path_pair.reverse()
    if path_pair[0] in cave_map.keys():
        if path_pair[1] != 'start':
            cave_map[path_pair[0]].append(path_pair[1])
    else:
        if path_pair[1] != 'start':
            cave_map[path_pair[0]] = [path_pair[1]]

# we don't want the end to have no possible next paths
cave_map['end'] = []

print(cave_map)
print()
distinct_paths = []


def multiple_small_traversed(next_path, cumulative_path):
    # if not small cave then just return 
    if not next_path.islower():
        return False

    if next_path == 'start':
        return True

    if cumulative_path.count(next_path) > 1:
        return True

    # get a list of all the unique caves we've visited so far
    unique_caves = list(set(cumulative_path.copy()))
    
    for unique_cave in unique_caves:
        # ignore big caves
        if not unique_cave.islower():
            continue

        if cumulative_path.count(next_path) == 1 and cumulative_path.count(unique_cave) > 1:
            return True

    return False    


def recursive_traverse(position, cumulative_path=None):
    if cumulative_path is None:
        cumulative_path = []
    possible_paths = cave_map[position]
    cumulative_path.append(position)
    if position == 'end':
        distinct_paths.append(cumulative_path.copy())
        return
    for next_path in possible_paths:
        if multiple_small_traversed(next_path, cumulative_path.copy()): # or (next_path.islower() and position.islower()):
            pass
        else:
            recursive_traverse(next_path, cumulative_path.copy())


recursive_traverse('start')

# [print(path) for path in distinct_paths]
print(len(distinct_paths))
