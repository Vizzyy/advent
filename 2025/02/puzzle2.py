from collections import Counter

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split(',')
# print(inputs)
inputs = [[int(item) for item in line.strip().split('-')] for line in inputs]
[print(item) for item in inputs]

invalid_ids = []


def parts(s: str, n: int):
    return [s[i:i+n] for i in range(0, len(s), n)]


for input in inputs:
    start = input[0] 
    end = input[1]
    for num in range(start, end + 1):
        breaker = False
        str_num = str(num)
        len_str_num = len(str_num)

        # start from zero because we can have repeated single digits
        for divisor in range(1, len_str_num):
            if breaker:
                break
            str_parts = parts(str_num, divisor)
            counted_parts = Counter(str_parts)

            if len(counted_parts.keys()) > 1:
                # more than one repeated phrase
                continue

            for key in counted_parts.keys():
                if counted_parts[key] > 1:
                    invalid_ids.append(int(str_num))
                    breaker = True
                    break

        if breaker:
            continue
        
print(f'sum: {sum(invalid_ids)}')