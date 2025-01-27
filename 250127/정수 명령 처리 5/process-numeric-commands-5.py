n = int(input())

a = []

for _ in range(n):
    command_line = input().split()

    if command_line[0] == 'push_back':
        a.append(int(command_line[1]))
    if command_line[0] == 'pop_back':
        a.pop()
    if command_line[0] == 'size':
        print(len(a))
    if command_line[0] == 'get':
        print( a[int(command_line[1]) - 1] )
