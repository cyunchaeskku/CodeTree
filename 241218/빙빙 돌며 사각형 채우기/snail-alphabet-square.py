drs, dcs = [0,1,0,-1],[1,0,-1,0]

n, m = map(int,input().split())

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < m

a = [ [0 for _ in range(m)] for _ in range(n) ]

dir_num = 0

'''
A = 65
ord('A')
chr(65)
Z = 90
'''
ascii_num = 65

r, c = 0, 0
a[r][c] = chr(ascii_num)
ascii_num += 1
cnt = 1

while True:
    nr, nc = r+drs[dir_num], c+dcs[dir_num]
    if in_range(nr, nc) and a[nr][nc] == 0:
        r, c = nr, nc
        a[r][c] = chr(ascii_num)
        ascii_num += 1
        cnt += 1
        if cnt >= n *m:
            break
        if ascii_num > 90:
            ascii_num = 65
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()