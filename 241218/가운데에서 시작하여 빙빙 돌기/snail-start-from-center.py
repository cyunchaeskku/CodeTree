import math

drs, dcs = [0,1,0,-1],[1,0,-1,0]

n = int(input())

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n

start  = math.ceil(n/2) - 1

a = [ [0 for _ in range(n)] for _ in range(n) ]

r, c = start, start
cnt = 1
a[r][c] = cnt
cnt += 1

dir_num = 0

while cnt <= n * n:
    nr, nc = r + drs[dir_num], c + dcs[dir_num]
    if in_range(nr, nc) and a[nr][nc] == 0:
        r, c = nr, nc
        a[r][c] = cnt
        cnt += 1
    else:
        dir_num -= 1
        if dir_num < 0:
            dir_num = 3

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()