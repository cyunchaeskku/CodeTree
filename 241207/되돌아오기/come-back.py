dxs, dys = [1,0,-1,0], [0,-1,0,1]

d = {}

d['E'] = 0
d['S'] = 1
d['W'] = 2
d['N'] = 3

n = int(input())

x, y = 0, 0 
ans = 0

for i in range(n):
    dir_str, dist = input().split()
    dist = int(dist)
    dir_num = d[dir_str]
    
    for j in range(dist):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        ans += 1
        if x == 0 and y == 0:
            print(ans)
            break

print(-1)
    
