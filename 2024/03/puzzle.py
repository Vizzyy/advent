import re
from functools import reduce
from operator import mul

with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip()

reg_exp = r'(mul\(\d{1,3},\d{1,3}\))'

instructions = re.findall(reg_exp, inputs)


def multiply(instruction):
    components = re.findall(r'(\d{1,3})', instruction)
    components = [int(component) for component in components]
    return reduce(mul, components)


total = 0
for instruction in instructions:
    total += multiply(instruction)

print(total)