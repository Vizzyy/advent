import re

with open('input.txt', 'r') as file:
    text = file.read()

inputs = text.split('\n\n')

# print(inputs)

sanitized_inputs = []

[sanitized_inputs.append(pa.replace("\n", " ")) for pa in inputs]

# [print(pa) for pa in sanitized_inputs]


valid_passport_count = 0

# print(len(sanitized_inputs))

failed_passports = []

eye_color = ['amb,' 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


for passport in sanitized_inputs:
    # print()
    # print(passport)

    d = dict(s.split(':') for s in passport.strip().split(" "))

    # print(d.keys())
    try:
        if 'byr' not in d.keys() or not 1920 <= int(d['byr']) <= 2002:
            # failed_passports.append(d)
            continue
        if 'iyr' not in d.keys() or not 2010 <= int(d['iyr']) <= 2020:
            # failed_passports.append(d)
            continue
        if 'eyr' not in d.keys() or not 2020 <= int(d['eyr']) <= 2030:
            # failed_passports.append(d)
            continue
        if 'hgt' not in d.keys() or re.search(r'\d*[cm|in]', d['hgt']) is None:
            failed_passports.append(d)
            continue
        units = d['hgt'][-2:]
        # print(units)
        if units == "cm":
            # print(d['hgt'][:-2])
            if not 150 <= int(d['hgt'][:-2]) <= 193:
                # failed_passports.append(d)
                continue
        if units == "in":
            # print(d['hgt'][:-2])
            if not 59 <= int(d['hgt'][:-2]) <= 76:
                # failed_passports.append(d)
                continue
        # print(d['hcl'])
        if 'hcl' not in d.keys() or re.search(r'#[0-9a-f]{6}', d['hcl']) is None:
            # failed_passports.append(d)
            continue

        # print(d['ecl'])
        if 'ecl' not in d.keys() or d['ecl'] not in str(eye_color):
            # failed_passports.append(d)
            continue
        if 'pid' not in d.keys() or re.search(r'[0-9]{9}', d['pid']) is None:
            # failed_passports.append(d)
            continue
        if 'cid' not in d.keys():
            pass

        # print("valid")
        valid_passport_count += 1
    except Exception as e:
        print(e)
        continue


[print(pa) for pa in failed_passports]
print(valid_passport_count)

