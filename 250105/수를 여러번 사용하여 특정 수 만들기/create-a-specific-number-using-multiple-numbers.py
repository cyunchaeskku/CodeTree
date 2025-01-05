import sys

a, b, c = map(int, input().split())

A_threshold = c // a
B_threshold = c // b

ans = -sys.maxsize

for i in range(A_threshold+1):
    for j in range(B_threshold+1):
        val = a * i + b * j
        if val > c:
            continue
        ans = max(ans, val)

print(ans)