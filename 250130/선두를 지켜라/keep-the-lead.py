import sys

n, m = map(int, input().split())
a = [0]
b = [0]

idx = 0
for i in range(n):
    v, t  = map(int, input().split())
    for j in range(t):
        a.append(a[idx] + v)
        idx += 1

idx = 0
for i in range(m):
    v, t  = map(int, input().split())
    for j in range(t):
        b.append(b[idx] + v)
        idx += 1

head = 0 # -1: A가 선두, 1: B가 선두
prev_head = 0
ans = 0
for i in range(len(a)):
    if a[i] > b[i]:
        head = -1
    elif a[i] < b[i]:
        head = 1
    if prev_head * head < 0:
        ans += 1
    prev_head = head

print(ans)
