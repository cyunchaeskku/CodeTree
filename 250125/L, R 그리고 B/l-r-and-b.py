import sys

drs, dcs = [0,1,0,-1],[1,0,-1,0]

a = [
    list(input())
    for _ in range(10)
]

B_index = (0,0)
L_index = (0,0)
R_index = (0,0)

for i in range(10):
    for j in range(10):
        if a[i][j] == 'B':
            B_index = (i,j)
        if a[i][j] == 'L':
            L_index = (i,j)
        if a[i][j] == 'R':
            R_index = (i,j)


# L에서 B로 가는 경로에 R이 없을 경우의 답
ans = abs( L_index[0] - B_index[0]) + abs( L_index[1] - B_index[1]) - 1

# R이 가로막고 있으면 돌아가야 함
if ( (L_index[0] == R_index[0] and R_index[0] == B_index[0]) or \
    (L_index[1] == R_index[1] and R_index[1] == B_index[1]) ) and \
    ( ((L_index[0] < R_index[0] and R_index[0] < B_index[0]) or (B_index[0] < R_index[0] and R_index[0] < L_index[0])) or \
    ((L_index[1] < R_index[1] and R_index[1] < B_index[1]) or (B_index[1] < R_index[1] and R_index[1] < L_index[1])) ):
    ans += 2
print(ans)
