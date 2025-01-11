import sys

n, k = map(int, input().split())
a = []

min_val = sys.maxsize
max_val = -sys.maxsize
for _ in range(n):
    temp = int(input())
    min_val = min(min_val, temp)
    max_val = max(max_val, temp)
    a.append(temp)

sorted_a = sorted(a)

ans = -sys.maxsize

for min_border in range(min_val, max_val):
    cnt = 0
    for i in range(n):
        if a[i] >= min_border and a[i] <= min_border+k:
            cnt += 1
    ans = max(ans, cnt)

print(ans)