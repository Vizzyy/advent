with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [game.split(' ') for game in inputs.strip().split('\n')]

total_score = 0
for match in inputs:
    match_score = 0
    if match[0] == "A": # rock
        if match[1] == "X":
            # lose with scissors
            match_score += 0 + 3
        if match[1] == "Y":
            # tie with rock
            match_score += 3 + 1
        elif match[1] == "Z":
            # win with paper
            match_score += 6 + 2
    if match[0] == "B": # paper
        if match[1] == "X":
            # lose with rock
            match_score += 0 + 1
        if match[1] == "Y":
            # tie with paper
            match_score += 3 + 2
        elif match[1] == "Z":
            # win with scissors
            match_score += 6 + 3
    if match[0] == "C": # scissors
        if match[1] == "X":
            # lose with paper
            match_score += 0 + 2
        if match[1] == "Y":
            # tie with scissors
            match_score += 3 + 3
        elif match[1] == "Z":
            # win with rock
            match_score += 6 + 1

    total_score += match_score

print(f'total_score: {total_score}')
