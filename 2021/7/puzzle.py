with open('input.txt', 'r') as file:
    puzzle_input = file.read().strip().split(',')

puzzle_input = [int(num) for num in puzzle_input]
puzzle_input.sort()

median_index = int(len(puzzle_input)/2)
median_value = puzzle_input[median_index]
average_value = int(sum(puzzle_input) / len(puzzle_input))
mode_value = max(set(puzzle_input), key=puzzle_input.count)
print(f"median_index: {median_index}, median_value: {median_value}, average_value: {average_value}, mode_value: {mode_value}")

least_fuel_used_value = 100000000
unique_input_numbers = list(set(puzzle_input))
print(unique_input_numbers)

for number_to_check in unique_input_numbers:  # number to check as shared value
    print(number_to_check)
    current_fuel_spent = 0
    fuel_increase_value = 1
    for number in puzzle_input:
        current_fuel_spent += abs(number - number_to_check)
        print(f"number: {number}, current_fuel_spent:{current_fuel_spent}")
        if current_fuel_spent > least_fuel_used_value:
            break
    if current_fuel_spent <= least_fuel_used_value:
        least_fuel_used_value = current_fuel_spent

print(f"least_fuel_used_value: {least_fuel_used_value}")


