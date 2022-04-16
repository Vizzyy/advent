with open('input.txt') as file:
    text = file.read().strip().split('\n')

chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

error_value = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

corrupted_rows = []
corrupted_letters = []

for row in text:
    stack = []
    for letter in row:
        # if letter is an "open" letter
        if letter in chars.keys():
            stack.append(letter)
        # if letter is a "close" letter
        else:
            if letter != chars[stack[-1]]:
                print(f"Expected {chars[stack[-1]]}, but found {letter} instead.")
                corrupted_letters.append(letter)
                corrupted_rows.append(row)
                break
            else:
                stack.pop(len(stack) - 1)

        # print(stack)

[print(row) for row in corrupted_rows]

result = 0
for letter in corrupted_letters:
    result += error_value[letter]

print(result)
