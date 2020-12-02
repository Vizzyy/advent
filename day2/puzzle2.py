with open('./passwords.txt', 'r') as file:
    inputs = file.readlines()

# print(inputs)

sanitized_inputs = []


for num in inputs:
    temp = num.replace("\n", "")
    parts = temp.split(' ')
    policy = parts[0].split('-')
    obj = {
        'lower_bound': policy[0],
        'upper_bound': policy[1],
        'letter': parts[1].replace(":", ""),
        'password': parts[2]
    }
    sanitized_inputs.append(obj)

# print(sanitized_inputs)

correct_passwords = 0

for pw in sanitized_inputs:
    num_letter = pw['password'].count(pw['letter'])
    if int(pw['lower_bound']) <= num_letter <= int(pw['upper_bound']):
        correct_passwords += 1
        # print(pw)

print(correct_passwords)

correct_passwords = 0

for pw in sanitized_inputs:

    p = pw['password']

    try:
        if (p[int(pw['lower_bound']) - 1] == pw['letter'] and not p[int(pw['upper_bound']) - 1] == pw['letter']) \
                or (not p[int(pw['lower_bound']) - 1] == pw['letter'] and p[int(pw['upper_bound']) - 1] == pw['letter']):
            correct_passwords += 1
            # print(pw)
    except Exception as e:
        print(e)
        print(pw)

print(correct_passwords)
