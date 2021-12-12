with open('input.txt', 'r') as file:
    puzzle_input = file.read().strip().split(',')

puzzle_input = [int(num) for num in puzzle_input]
# puzzle_input.sort()

median_index = int(len(puzzle_input)/2)
median_value = puzzle_input[median_index]
average_value = int(sum(puzzle_input) / len(puzzle_input))
mode_value = max(set(puzzle_input), key=puzzle_input.count)
print(f"median_index: {median_index}, median_value: {median_value}, average_value: {average_value}, mode_value: {mode_value}")

least_fuel_used_value = 1000000000000000000
unique_input_numbers = list(set(puzzle_input))
print(unique_input_numbers)

fuel_levels = [int(level) for level in range(0, 2000)]
fuel_chart = [sum(fuel_levels[0:level]) for level in fuel_levels]
print(fuel_chart)

for number_to_check in range(0, unique_input_numbers[len(unique_input_numbers) - 1]):  # number to check as shared value
    print(f"target: {number_to_check}")
    current_fuel_spent = 0
    for number in puzzle_input:
        abs_difference = abs(number - number_to_check)
        chart_index = abs_difference + 1
        current_fuel_spent += fuel_chart[chart_index]
        print(f"number: {number}, abs_difference: {abs_difference}, fuel_chart[abs_difference]: {fuel_chart[chart_index]}, current_fuel_spent:{current_fuel_spent}")
        if current_fuel_spent > least_fuel_used_value:
            break
    if current_fuel_spent <= least_fuel_used_value:
        least_fuel_used_value = current_fuel_spent

print(f"least_fuel_used_value: {least_fuel_used_value}")


