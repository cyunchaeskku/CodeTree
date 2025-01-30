import sys

n, m = map(int, input().split())

a = [0]
b = [0]

idx = 0
for i in range(n):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if d == 'L':
            a.append(a[idx] - 1)
            idx += 1
        else:
            a.append(a[idx] + 1)
            idx += 1
    
idx = 0
for i in range(m):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if d == 'L':
            b.append(b[idx] - 1)
            idx += 1
        else:
            b.append(b[idx] + 1)
            idx += 1

ans = 0
i,j = 0,0
flag = True


while i < min(len(a), len(b)) and j < min(len(a), len(b)):
    if i == 0 and j == 0:
        i += 1
        j += 1
        continue
    else:
        if a[i] == b[i]:
            if flag == False:
                ans += 1
            flag = True
            i += 1
            j += 1
        else:
            flag = False
            i += 1
            j += 1


if len(a) > len(b):
    j -= 1
    while i < len(a):
        if a[i] == b[j]:
            if flag == False:
                ans += 1
            flag = True
            i += 1
        else:
            flag = False
            i += 1
else:
    i -= 1
    while j < len(b):
        if a[i] == b[j]:
            if flag == False:
                ans += 1
            flag = True
            j += 1
        else:
            flag = False
            j += 1            
print(ans)