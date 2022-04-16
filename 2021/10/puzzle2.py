import math

with open('input.txt') as file:
    text = file.read().strip().split('\n')

chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

error_value = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

corrupted_rows = []
incomplete_rows = []
corrupted_letters = []
autocompletes = []

for row in text:
    stack = []
    corrupted = False
    for letter in row:
        # if letter is an "open" letter
        if letter in chars.keys():
            stack.append(letter)
        # if letter is a "close" letter
        else:
            # if the closing letter is not the correct one
            if letter != chars[stack[-1]]:
                # print(f"Expected {chars[stack[-1]]}, but found {letter} instead.")
                corrupted_letters.append(letter)
                corrupted_rows.append(row)
                corrupted = True
                break
            else:
                stack.pop(len(stack) - 1)
    if not corrupted:
        incomplete_rows.append(row)
        autocompletes.append(stack.copy())
        # print(stack)


[print(row) for row in incomplete_rows]
print()
[print(stack) for stack in autocompletes]

autocomplete_scores = []

for stack in autocompletes:
    score = 0
    stack.reverse()
    for letter in stack:
        score *= 5
        score += error_value[letter]

    autocomplete_scores.append(score)

print(autocomplete_scores)

autocomplete_scores.sort()

print(autocomplete_scores)

middle = math.floor(len(autocomplete_scores)/2)

print(f"Middle score: {autocomplete_scores[middle]}")
