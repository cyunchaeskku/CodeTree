dxs, dys = [0,1,0,-1], [1,0,-1,0]

n = int(input())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

a = []



for i in range(n):
    temp = input()
    temp_list = []
    for j in range(len(temp)):
        temp_list.append(temp[j])
    a.append(temp_list)

k = int(input())

dir_num = -1
r,c = -1, -1
ans = 0

if 1 <= k and k <= n:
    dir_num = 1
    r = 0
    c = k-1
if n+1 <= k and k <= 2*n:
    dir_num = 2
    r = k - n -1
    c = n-1
if 2*n+1 <= k and k <= 3*n:
    dir_num = 3
    r = n-1
    c = (n-1) - (k - (2*n) - 1)
if 3*n+1 <= k and k <= 4*n:
    dir_num = 0
    r = (n-1) - (k - 3*n - 1)
    c = 0


if a[r][c] == '/':
    if dir_num == 0 or dir_num == 2:
        dir_num-=1
        if dir_num<0:
            dir_num = 3
    elif dir_num == 1 or dir_num == 3:
        dir_num = (dir_num+1)%4
else:
    if dir_num == 0 or dir_num == 2:
        dir_num = (dir_num+1)%4
    elif dir_num == 1 or dir_num == 3:
        dir_num-=1
        if dir_num<0:
            dir_num = 3
ans += 1
while True:
    r, c = r + dxs[dir_num], c + dys[dir_num]
    if not in_range(r,c):
        break
    if a[r][c] == '/':
        if dir_num == 0 or dir_num == 2:
            dir_num-=1
            if dir_num<0:
                dir_num = 3
        elif dir_num == 1 or dir_num == 3:
            dir_num = (dir_num+1)%4
    else:
        if dir_num == 0 or dir_num == 2:
            dir_num = (dir_num+1)%4
        elif dir_num == 1 or dir_num == 3:
            dir_num-=1
            if dir_num<0:
                dir_num = 3
    ans += 1
    
print(ans)





'''
\ -> dir_num이 0이거나 2이면, 오른쪽으로 90도 회전, dir_num이 1이거나 3면 왼쪽으로 90도 회전
/ -> dir_num이 0이거나 2이면, 왼쪽으로 90도 회전, dir_num이 1이거나 3면 오른쪽으로 90도 회전

k=2 -> 0,1

0,0 0,1 0,2
1,0     1,2
2,0 2,1 2,2
'''

