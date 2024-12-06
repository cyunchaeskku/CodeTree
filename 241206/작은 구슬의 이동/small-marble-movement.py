dxs, dys = [0,1,-1,0], [1,0,0,-1]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

n, t = map(int, input().split())
x, y, dir_str = input().split()

x= int(x)
y= int(y)

d = {}
d['R'] = 0
d['D'] = 1
d['U'] = 2
d['L'] = 3

dir_num = d[dir_str]

nx = x
ny = y

for i in range(t):
    # print(dir_num)
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    # print(nx, ny)
    if in_range(nx, ny):
        x = nx
        y = ny
    else:
        dir_num = 3-dir_num

print(x, y)