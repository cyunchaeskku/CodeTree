import sys

n, m = map(int, input().split())

ans = -sys.maxsize
for i in range(1, max(n, m)):
    if n % i == 0 and m % i == 0:
        ans = max(ans, i)

print(ans)