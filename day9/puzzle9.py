with open('./input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(int(temp))

# print(sanitized_inputs)

main_ptr = 25
sub_array_lo_ptr = 0
sub_array_hi_ptr = 25
number = None

for i in range(main_ptr, len(sanitized_inputs)):
    # print(f"target = {sanitized_inputs[main_ptr]}")
    match = False

    preamble = sanitized_inputs[sub_array_lo_ptr:sub_array_hi_ptr]
    preamble.sort()
    # print(preamble)

    for x in preamble:
        for y in preamble:
            if x == y:
                continue
            if x + y == sanitized_inputs[main_ptr]:
                # print(f"{x} + {y} = {sanitized_inputs[main_ptr]}")
                match = True
                break

    if not match:
        print("no match")
        break
    else:
        main_ptr += 1
        sub_array_lo_ptr += 1
        sub_array_hi_ptr += 1


invalid_number = sanitized_inputs[main_ptr]
print(invalid_number)

# Part two

main_ptr = 0
lo = hi = -1


for i in range(len(sanitized_inputs)):
    temp_total = 0
    for j in range(i, len(sanitized_inputs)):
        temp_total += sanitized_inputs[j]
        if temp_total > invalid_number:
            break
        if temp_total == invalid_number:
            lo = i
            hi = j
            break
    if lo > -1 < hi:
        break

print((lo, hi))
consecutive_nums = sanitized_inputs[lo:hi]
print(consecutive_nums)
consecutive_nums.sort()
print(consecutive_nums)
print(consecutive_nums[0], consecutive_nums[len(consecutive_nums)-1])
print(consecutive_nums[0] + consecutive_nums[len(consecutive_nums)-1])



