import sys

n = int(input())
x1s, x2s = [], []
for _ in range(n):
    x1, x2 = map(int, input().split())
    x1s.append(x1)
    x2s.append(x2)

ans = sys.maxsize
for i in range(n):
    lo, hi = sys.maxsize, -sys.maxsize
    for j in range(n):
        if j == i:
            continue
        lo = min(lo, x1s[j])
        hi = max(hi, x2s[j])
    ans = min(ans, hi - lo)
print(ans)
        