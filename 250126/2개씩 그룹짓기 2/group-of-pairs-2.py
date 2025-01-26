import sys

n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = sys.maxsize
for i in range(n):
    ans = min(ans, a[i+n] - a[i])

print(ans)