import sys

ans = sys.maxsize

n,m = map(int, input().split())

for i in range(min(n, m), n *m  + 1):
    if i % n == 0 and i % m == 0:
        ans = min(ans, i)

print(ans)