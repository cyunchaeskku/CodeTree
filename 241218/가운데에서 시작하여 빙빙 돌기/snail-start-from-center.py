import math

drs, dcs = [0,1,0,-1],[1,0,-1,0]

n = int(input())

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n

start  = math.ceil(n/2) - 1

a = [ [0 for _ in range(n)] for _ in range(n) ]

r, c = n-1,n-1
cnt = n * n
a[r][c] = cnt
cnt -= 1

dir_num = 0

while cnt >= 1:
    nr, nc = r + drs[dir_num], c + dcs[dir_num]
    if in_range(nr, nc) and a[nr][nc] == 0:
        r, c = nr, nc
        a[r][c] = cnt
        cnt -= 1
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()