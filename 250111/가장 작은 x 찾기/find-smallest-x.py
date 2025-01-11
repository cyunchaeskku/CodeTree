import sys

n = int(input())

a = []
b = []

for _ in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

ans = sys.maxsize

for i in range(max(a[0]//2,1), b[0]//2 + 1):
    start = i
    success = True
    start *= 2
    for j in range(n):
        if start < a[j] or start > b[j]:
            success = False
            break
        else:
            start *= 2
    if success == True:
        ans = min(i, ans)

print(ans)
