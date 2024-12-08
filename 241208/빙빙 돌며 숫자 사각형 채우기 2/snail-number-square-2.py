drs, dcs = [0,1,0,-1], [1,0,-1,0]

n, m = map(int, input().split())

arr = [ [0 for _ in range(m)] for _ in range(n) ]

def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < m


cnt = 1
dir_num = 1
r, c = 0, 0
arr[r][c] = cnt
cnt += 1

while cnt <= n *m:
    nr, nc = r + drs[dir_num], c + dcs[dir_num]
    if in_range(nr,nc) and arr[nr][nc] == 0:
        arr[nr][nc] = cnt
        cnt += 1
        r, c= nr, nc
    else:
        dir_num = (dir_num+1)%4

for i in range (n):
    for j in range (m):
        print(arr[i][j],end=' ')
    print()