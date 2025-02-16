class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def size(self):
        return len(self.items)

    def pop(self):
       
        return self.items.pop()

    def top(self):
        
        return self.items[self.size() - 1]

s = Stack()

n = int(input())
for _ in range(n):
    command_line = input().split()

    if command_line[0] == 'push':
        s.push(int(command_line[1]))
    if command_line[0] == 'size':
        print(s.size())
    if command_line[0] == 'pop':
        print(s.pop())
    if command_line[0] == 'empty':
        print(s.empty())
    if command_line[0] == 'top':
        print(s.top())