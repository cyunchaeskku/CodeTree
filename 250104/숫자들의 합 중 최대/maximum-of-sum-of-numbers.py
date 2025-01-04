import sys

ans = -sys.maxsize

x, y = map(int, input().split())

for n in range(x, y+1):
    a = tuple(map(int, list(str(n))))
    ans = max(ans, sum(a))
print(ans)