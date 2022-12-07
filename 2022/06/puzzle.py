with open('input.txt', 'r') as file:
    inputs = file.read()
inputs = inputs.strip().split('\n')[0]

array = []
for char in range(len(inputs)):
    try:
        substring = inputs[char:char+4]
        print(substring)
        dupes = list(set(filter(lambda x: substring.count(x) >= 2, substring)))
        print(f'dupes: {dupes}')

        if len(dupes) == 0:
            print(char + 4)
            break
    except:
        pass

