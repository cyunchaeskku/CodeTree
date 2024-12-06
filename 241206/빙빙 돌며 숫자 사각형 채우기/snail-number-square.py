dxs, dys =  [0,1,0,-1], [1,0,-1,0]

def in_range(x, y):
    return 1 <= x and x <= r and 1 <= y and y <= c
'''
'''

r, c = map(int, input().split())

a = []
for j in range(r):
    temp = []
    for i in range(c):
        temp.append(0)
    a.append(temp)
# print(a)


'''
1,6 (0,5)
2,6 (1,5)

'''

x, y = 1, 1

cnt = 1
a[x-1][y-1] = cnt
cnt += 1

# print(a)

dir_num = 0

while cnt <= r * c:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if in_range(nx, ny) and a[nx-1][ny-1] == 0:
        a[nx-1][ny-1] = cnt
        cnt += 1
        x, y= nx, ny
    else:
        dir_num = (dir_num+1)%4

for i in range(r):
    for j in range(c):
        print(a[i][j],end=' ')
    print()