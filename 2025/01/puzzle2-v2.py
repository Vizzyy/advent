with open('input.txt', 'r') as file:
    inputs = file.read()

inputs = inputs.strip().split('\n')
inputs = [[line[0], int(line[1:])] for line in inputs]
# print(inputs)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Dial:
    zero_pos_count = 0
    
    def __init__(self, size):
        self.size = size
        self.nodes = [Node(i) for i in range(size)]
        for i, node in enumerate(self.nodes):
            node.prev = self.nodes[(i - 1) % size]
            node.next = self.nodes[(i + 1) % size]
        self.current = self.nodes[0]

    def get_node(self, value):
        return self.nodes[value % self.size]

    def move(self, steps):
        if steps >= 0:
            for _ in range(steps):
                self.current = self.current.next
                if self.current.value == 0:
                    self.zero_pos_count += 1
        else:
            for _ in range(-steps):
                self.current = self.current.prev
                if self.current.value == 0:
                    self.zero_pos_count += 1
        return self.current

    def to_list(self):
        out = []
        node = self.nodes[0]
        for _ in range(self.size):
            out.append(node.value)
            node = node.next
        return out

dial = Dial(100)

dial.current = dial.get_node(50)

for instruction in inputs:
    if instruction[0] == 'L':
        dial.move(-instruction[1])
    elif instruction[0] == 'R':
        dial.move(instruction[1])
    else:
        raise ValueError(f"Unknown direction: {instruction[0]}")

print(dial.zero_pos_count)

# 6858 (correct)