with open('test.txt') as file:
    input_text = file.read().strip().split('\n')

input_text = [[int(coord) for coord in line.split(',')] for line in input_text]    

print(input_text)

max_x = 11
max_y = 15

paper = [['.' for x in range(max_x)] for y in range(max_y)]

print()
[print(line) for line in paper] 

for dot in input_text:
    paper[dot[1]][dot[0]] = '#'

print()
[print(line) for line in paper] 
