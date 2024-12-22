import sys

# drs, dcs = [0,1,0,-1],[1,0,-1,0]

drs, dcs = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

def in_range(r, c):
    return 0 <= r and r < 19 and 0 <= c and c < 19

a = []

for i in range(19):
    for j in range(19):
        a.append( list(map(int,sys.stdin.readline().rstrip().split()) ) )

win = 0 # 0:tie, 1: black win, 2: white win
dir_num = -1

for i in range(19):
    for j in range(19):
        if a[i][j] != 0:
            for k in range(8):
                ni, nj = i + drs[k], j + dcs[k]
                if in_range(ni, nj) and a[ni][nj] == a[i][j]:
                    dir_num = k
                    break
            r, c = i, j
            cnt = 0
            for k in range(5):
                nr, nc = r + drs[dir_num], c + dcs[dir_num]
                if in_range(nr,nc) and a[nr][nc] == a[r][c]:
                    r, c = nr, nc
                    cnt += 1
            if cnt == 4:
                print(a[r][c])
                dir_num = (dir_num+4)%8
                nr, nc = r + 2 * drs[dir_num], c + 2 * dcs[dir_num]
                print(nr+1, nc+1)
                exit(0)


print(0)