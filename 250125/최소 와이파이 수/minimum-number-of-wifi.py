import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

wifi = [False for _ in range(n)]

# m 거리까지는 wifi 사용 가능하므로.
for i in range(0 + m, n - m):
    if True in wifi[i-m:i+m+1]:
        continue
    if 1 in a[i-m:i+m+1]:
        ans += 1
        for j in range(i-m, i+m+1):
            wifi[j] = True
print(ans)
