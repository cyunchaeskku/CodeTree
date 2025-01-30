import sys

n, m = map(int, input().split())
a = [0]
b = [0]

idx = 0
for i in range(n):
    v, t = map(int, input().split())
    for j in range(t):
        a.append( a[idx] + v )
        idx += 1

idx = 0
for i in range(m):
    v, t = map(int, input().split())
    for j in range(t):
        b.append( b[idx] + v )
        idx += 1

# print(a)
# print(b)

head = 0
prev_head = 0 # -1: A, 1:B
ans = 0
for i in range(len(a)):
    if a[i] > b[i]:
        head = -1
    elif a[i] < b[i]:
        head = 1
    else:
        head = 0
    if head != prev_head:
        ans += 1
    prev_head = head




# ------ answer -------- #
print(ans)