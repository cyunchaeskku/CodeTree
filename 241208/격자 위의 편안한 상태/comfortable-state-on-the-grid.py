drs, dcs = [0,-1,0,1], [1,0,-1,0]

n,m = map(int, input().split())

a = [ [0 for _ in range(n)] for _ in range(n) ]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

for i in range(m):
    cnt = 0
    r, c = map(int, input().split())
    a[r-1][c-1] = 1
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and a[nr-1][nc-1] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)