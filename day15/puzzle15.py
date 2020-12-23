with open('./input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = []

for line in inputs:
    temp = line.split(',')
    sanitized_inputs.append([int(num) for num in temp])

# Key = Number , Value = Last Turn Spoken
numbers_spoken = {}
current_turn = 0
last_num_spoken = 0
last_num_new = True

for num in sanitized_inputs[0]:
    current_turn += 1
    numbers_spoken[num] = [current_turn]
    last_num_spoken = num

print(numbers_spoken)
print(last_num_spoken)

while current_turn <= 2020:
    current_turn += 1

    last_spoken = numbers_spoken[last_num_spoken]
    if len(last_spoken) == 1:
        if current_turn != 2021:
            last_num_spoken = 0  # new number was spoken last turn
    else:
        last_num_spoken = last_spoken[len(last_spoken) - 1] - last_spoken[len(last_spoken) - 2]

    current_keys = numbers_spoken.keys()
    if last_num_spoken == 0 and last_num_spoken not in current_keys:
        # 0 doesn't exist yet in map
        numbers_spoken[last_num_spoken] = [current_turn]
    else:
        if last_num_spoken not in current_keys:
            numbers_spoken[last_num_spoken] = [current_turn]
        else:
            numbers_spoken[last_num_spoken] = numbers_spoken[last_num_spoken] + [current_turn]

print(f"current_turn: {current_turn}, last_num_spoken: {last_num_spoken}")



