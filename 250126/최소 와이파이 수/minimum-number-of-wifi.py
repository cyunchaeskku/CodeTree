import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans, i = 0, 0

while i < n:
    if a[i] == 1:
        ans += 1
        i += 2 * m + 1
    else:
        i += 1

print(ans)