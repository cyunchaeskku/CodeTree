import sys

ans = -sys.maxsize

x, y = map(int, input().split())

for n in range(x, y+1):
    d1, d2 = tuple(map(int, list(str(n))))
    ans = max(ans, d1 + d2)
print(ans)