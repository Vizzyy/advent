import re
from functools import reduce
from operator import mul

with open('input2.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip()

split_input = re.split("(do\(\))|(don't\(\))", inputs)

split_input = [item for item in split_input if item is not None]

good_inputs = []    
last_input_bad = False
for input in split_input:
    if not last_input_bad and input != "don't()":
        good_inputs.append(input)
    elif input == "do()":
        last_input_bad = False
    else:
        last_input_bad = True

good_input = ''.join(good_inputs)

# rest is the same as part 1

reg_exp = r'(mul\(\d{1,3},\d{1,3}\))'

instructions = re.findall(reg_exp, good_input)


def multiply(instruction):
    components = re.findall(r'(\d{1,3})', instruction)
    components = [int(component) for component in components]
    return reduce(mul, components)


total = 0
for instruction in instructions:
    total += multiply(instruction)

print(total)