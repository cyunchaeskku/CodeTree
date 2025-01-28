import sys

n, m = map(int, input().split())

a = [0]
b = [0]

idx = 1
for i in range(1,n+1):
    d, t = input().split()
    t = int(t)
    for j in range(t):
        if d == 'L':
            a.append(a[idx-1] - 1)
        else:
            a.append(a[idx-1] + 1)
        idx += 1

idx = 1
for i in range(1, m+1):
    d, t = input().split()
    t = int(t)
    for j in range(t):
        if d == 'L':
            b.append(b[idx-1] - 1)
        else:
            b.append(b[idx-1] + 1)
        idx += 1

flag = False
for i in range(min(len(a), len(b))):
    if i > 0:
        if a[i] == b[i]:
            print(i)
            flag = True
            break

if flag == False:
    print(-1)