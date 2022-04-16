with open('input.txt', 'r') as file:
    starting_row = file.readline()

lantern_fish = [int(fish) for fish in starting_row.strip().split(',')]

print(lantern_fish)

day_counter = 0
while True:
    for fish_idx in range(len(lantern_fish)):
        if lantern_fish[fish_idx] == 0:
            lantern_fish[fish_idx] = 6
            lantern_fish.append(8)
        else:
            lantern_fish[fish_idx] = lantern_fish[fish_idx] - 1
    day_counter += 1
    print(f"day_counter: {day_counter} - len(lantern_fish): {len(lantern_fish)}")
    if day_counter == 80:
        break
