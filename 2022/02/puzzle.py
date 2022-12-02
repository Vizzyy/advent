with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = [game.split(' ') for game in inputs.strip().split('\n')]

total_score = 0
for match in inputs:
    match_score = 0
    if match[0] == "A": # rock
        if match[1] == "X": # rock
            # tie
            match_score += 3 + 1
        if match[1] == "Y":
            # win
            match_score += 6 + 2
        elif match[1] == "Z":
            # lose
            match_score += 0 + 3
    if match[0] == "B": # paper
        if match[1] == "X": # rock
            # lose
            match_score += 0 + 1
        if match[1] == "Y": # paper
            # tie
            match_score += 3 + 2
        elif match[1] == "Z": # scissors
            # win
            match_score += 6 + 3
    if match[0] == "C": # scissors
        if match[1] == "X":
            # win
            match_score += 6 + 1
        if match[1] == "Y":
            # lose
            match_score += 0 + 2
        elif match[1] == "Z":
            # tie
            match_score += 3 + 3

    total_score += match_score

print(f'total_score: {total_score}')
