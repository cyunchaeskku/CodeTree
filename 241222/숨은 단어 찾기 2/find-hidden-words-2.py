import sys

drs, dcs = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

n, m = map(int, input().split())

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < m

a = []

for i in range(n):
    a.append(list(input().rstrip()))

cnt = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            r, c = i, j
            for k in range(8):
                nr, nc = r + drs[k], c + dcs[k]
                if in_range(nr, nc) and a[nr][nc] == 'E':
                    dir_num = k
                    nnr, nnc = nr + drs[dir_num], nc + dcs[dir_num]
                    if in_range(nnr, nnc) and a[nnr][nnc] == 'E':
                        # print(r, c)
                        cnt += 1

print(cnt)