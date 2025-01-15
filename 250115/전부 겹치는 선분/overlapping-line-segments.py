import sys

n = int(input())
a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_x1 = -sys.maxsize
min_x2 = sys.maxsize

for i in range(n):
    x1, x2 = a[i]
    max_x1 = max(max_x1, x1)
    min_x2 = min(min_x2, x2)

if max_x1 > min_x2:
    print("No")
else:
    print("Yes")
    