with open('./puzzle1_input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(int(temp))

sanitized_inputs.sort()

print(sanitized_inputs)


def puzzle1():
    count = 0

    for i in range(len(sanitized_inputs)):
        for j in range(len(sanitized_inputs)):
            if i == j:
                continue
            if sanitized_inputs[i] + sanitized_inputs[j] == 2020:
                print(f"{count} comparisons")
                return sanitized_inputs[i], sanitized_inputs[j]
            count += 1
    return "Not found"


def part2():
    count = 0

    for i in range(len(sanitized_inputs)):
        for j in range(len(sanitized_inputs)):
            if j == i:
                continue
            for y in range(len(sanitized_inputs)):
                if y == j or y == i:
                    continue
                if sanitized_inputs[i] + sanitized_inputs[j] + sanitized_inputs[y] == 2020:
                    print(f"{count} comparisons")
                    return sanitized_inputs[i], sanitized_inputs[j], sanitized_inputs[y]
                count += 1
    return 0, 0, 0


result = puzzle1()
print(result)
print(result[0] * result[1])
# O N^2 , but given the sorted dataset only takes 407 comparisons


result2 = part2()
print(result2)
print(result2[0] * result2[1] * result2[2])
# O N^3 , but given the sorted dataset only takes 138 comparisons
