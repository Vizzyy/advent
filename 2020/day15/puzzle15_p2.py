from datetime import datetime

with open('input.txt', 'r') as file:
    inputs = file.readlines()

sanitized_inputs = []

for line in inputs:
    temp = line.split(',')
    sanitized_inputs.append([int(num) for num in temp])

numbers_spoken = [None] * 30000000
current_turn = 1
last_num_spoken = 0
last_num_new = True

for num in sanitized_inputs[0]:
    numbers_spoken[num] = current_turn
    last_num_spoken = num
    current_turn += 1

repeat_num_diff = 0

start_time = datetime.now()

while current_turn <= len(numbers_spoken):

    if last_num_new:
        last_num_spoken = 0  # new number was spoken last turn
    else:
        last_num_spoken = repeat_num_diff

    if numbers_spoken[last_num_spoken] is not None:
        last_num_new = False
        repeat_num_diff = current_turn - numbers_spoken[last_num_spoken]
    else:
        last_num_new = True

    numbers_spoken[last_num_spoken] = current_turn

    current_turn += 1


end_time = datetime.now()
print(f"indexOf: {numbers_spoken.index(len(numbers_spoken))}")
# print(end_time)
elapsed_time = end_time - start_time
print(elapsed_time)




