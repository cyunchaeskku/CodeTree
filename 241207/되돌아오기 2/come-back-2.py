dxs, dys = [1,0,-1,0], [0,-1,0,1]

dir_num = 3
ans = 0
x, y = 0,0 

command = input().rstrip()

for i in range(len(command)):
    if x == 0 and y == 0 and ans:
        print(ans)
        exit(0)
    if command[i] == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    if command[i] == 'R':
        dir_num = (dir_num+1) % 4
    if command[i] == 'L':
        dir_num = dir_num-1
        if dir_num < 0:
            dir_num = 3
    ans += 1
if x == 0 and y == 0:
    print(ans) 
else:
    print(-1)
