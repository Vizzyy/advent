import copy

with open('./input.txt', 'r') as file:
    text = file.read()

inputs = text.split('\n\n')

print(inputs)

sanitized_inputs = []

[sanitized_inputs.append(pa.replace("\n", " ")) for pa in inputs]

# [print(pa) for pa in sanitized_inputs]


valid_passport_count = 0

print(len(sanitized_inputs))

failed_passports = []

for passport in sanitized_inputs:
    print()
    print(passport)

    d = dict(s.split(':') for s in passport.strip().split(" "))

    print(d.keys())
    if 'byr' not in d.keys():
        failed_passports.append(d)
        continue
    if 'iyr' not in d.keys():
        failed_passports.append(d)
        continue
    if 'eyr' not in d.keys():
        failed_passports.append(d)
        continue
    if 'hgt' not in d.keys():
        failed_passports.append(d)
        continue
    if 'hcl' not in d.keys():
        failed_passports.append(d)
        continue
    if 'ecl' not in d.keys():
        failed_passports.append(d)
        continue
    if 'pid' not in d.keys():
        failed_passports.append(d)
        continue
    if 'cid' not in d.keys():
        pass

    print("valid")
    valid_passport_count += 1


print(valid_passport_count)

