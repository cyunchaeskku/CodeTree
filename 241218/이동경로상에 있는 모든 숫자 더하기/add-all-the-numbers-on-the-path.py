import math

nrs, ncs = [0,1,0,-1],[1,0,-1,0]

n, t = map(int, input().split())
commands = input().rstrip()


def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n

a = []
for i in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)

ans = 0
dir_num = 3
r, c = math.ceil(n/2) - 1, math.ceil(n/2) - 1
ans += a[r][c]

for iter in range(t):
    command = commands[iter]

    if command == 'F':
        nr, nc = r + nrs[dir_num], c + ncs[dir_num]
        if in_range(nr, nc):
            r, c = nr, nc
            ans += a[r][c]


    if command == 'L':
        dir_num -= 1
        if dir_num < 0:
            dir_num = 3
    if command == 'R':
        dir_num = (dir_num+1)%4

print(ans)

'''
5+6+3+2
'''
