import sys

n = int(input())

a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = a[i]
        x2, y2 = a[j]

        val = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
        ans = min(val, ans)

print(ans)