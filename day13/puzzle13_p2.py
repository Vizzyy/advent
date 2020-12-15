from functools import reduce

with open('./input.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []

for num in inputs:
    temp = num.replace("\n", "")
    sanitized_inputs.append(temp)

# [print(''.join(x)) for x in sanitized_inputs]
# print(sanitized_inputs)
# print()

timestamp_start = int(sanitized_inputs[0])
options = sanitized_inputs[1].split(',')
options_parsed = [int(x) for x in options if x != "x"]
# options_parsed.sort()
# print(timestamp_start)
# print(options_parsed)


# NAIVE solution

# timestamp_mod = copy(timestamp_start)
# timestamp_mod = 100000000000000
# result = None
# while not result:
#     found = 0
#     for option in options:
#         if option == "x":
#             continue
#         index = options.index(option)
#         if (timestamp_mod + index) % int(option) == 0:
#             found += 1
#             continue
#         else:
#             break
#
#     if found == len(options_parsed):
#         result = timestamp_mod
#
#     if not result:
#         timestamp_mod += 1
#
#
# print(result)
# print(f"time end: {timestamp_mod}")
# print(result * (timestamp_mod - timestamp_start))


# Chinese Remainder Theorem implementation pulled from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


print(options_parsed)
# This line was the key
remainders = [bus - options.index(str(bus)) for bus in options_parsed]
print(remainders)

print(chinese_remainder(options_parsed, remainders))
