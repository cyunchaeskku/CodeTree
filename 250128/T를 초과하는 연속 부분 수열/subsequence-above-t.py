import sys

n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = - sys.maxsize
cnt = 0

for i in range(n):
    if i == 0:
        if a[i] > t:
            cnt = 1
    else:
        if a[i] > t and a[i] > a[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            if a[i] > t:
                cnt = 1
            else:
                cnt = 0

ans = max(ans, cnt)

print(ans)