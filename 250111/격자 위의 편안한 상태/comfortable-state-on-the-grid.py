import sys

n, m = map(int, input().split())

a = [ [0 for _ in range(n)] for _ in range(n) ]

dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

for i in range(m):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    a[r][c] = 1
    cnt = 0
    for j in range(4):
        nr, nc = r + dxs[j], c + dys[j]
        if in_range(nr, nc) and a[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)

