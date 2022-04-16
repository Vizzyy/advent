import datetime

with open('input.txt', 'r') as file:
    starting_row = file.readline()

lantern_fish = [int(fish) for fish in starting_row.strip().split(',')]

# print(lantern_fish)

time_start = datetime.datetime.now()

lantern_fish.sort()
# print(lantern_fish)
lantern_fish_map = {x: lantern_fish.count(x) for x in lantern_fish}
print(lantern_fish_map)

day_counter = 0

for day in range(256):
    t_fish_map = {}
    for fish_type in lantern_fish_map.keys():
        if fish_type == 0:
            t_fish_map[8] = lantern_fish_map[0]
            t_fish_map[6] = lantern_fish_map[0]
        else:
            if fish_type-1 not in t_fish_map.keys():
                t_fish_map[fish_type - 1] = lantern_fish_map[fish_type]
            else:
                t_fish_map[fish_type - 1] = t_fish_map[fish_type - 1] + lantern_fish_map[fish_type]

    lantern_fish_map = dict(sorted(t_fish_map.items()))
    print(f"day {day} - lantern_fish_map: {lantern_fish_map}")


total_fish = 0
for fish_type in lantern_fish_map.keys():
    total_fish += lantern_fish_map[fish_type]

print(total_fish)
print(f"finished in: {datetime.datetime.now() - time_start}")
