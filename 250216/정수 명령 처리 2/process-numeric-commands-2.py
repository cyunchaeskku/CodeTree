'''
push
size
empty
front
pop
'''

from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        return self.dq.popleft()

    def front(self):
        return self.dq[0]

q = Queue()

n = int(input())
for _ in range(n):
    command_line = input().split()
    if command_line[0] == 'push':
        q.push(int(command_line[1]))
    if command_line[0] == 'pop':
        print(q.pop())
    if command_line[0] == 'size':
        print(q.size())
    if command_line[0] == 'empty':
        print(int(q.empty()))
    if command_line[0] == 'front':
        print(q.front())