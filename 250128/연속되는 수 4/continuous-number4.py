import sys

n = int(input())
a = [
    int(input())
    for _ in range(n)
]

ans = -sys.maxsize

cnt = 1

for i in range(n):
    if i > 0:
        if a[i] > a[i - 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
ans = max(ans, cnt)
print(ans)