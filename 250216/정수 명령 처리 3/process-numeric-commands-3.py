'''
dq.appendleft

dq.append

dq.popleft -> front

dq.pop

len(dq)

if dq

dq[0] -> front

dq[-1] -> back

'''

from collections import deque

dq = deque()

n = int(input())
for _ in range(n):
    command_line = input().split()
    if command_line[0] == 'push_front':
        dq.appendleft(int(command_line[1]))
    if command_line[0] == 'push_back':
        dq.append(int(command_line[1]))
    if command_line[0] == 'pop_front':
        print(dq.popleft())
    if command_line[0] == 'pop_back':
        print(dq.pop())
    if command_line[0] == 'size':
        print(len(dq))
    if command_line[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    if command_line[0] == 'front':
        print(dq[0])
    if command_line[0] == 'back':
        print(dq[-1])

