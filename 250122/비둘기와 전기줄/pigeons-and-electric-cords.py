import sys

n = int(input())

pigeons = [[] for _ in range(11)]


for _ in range(n):
    a, b = map(int, input().split())
    pigeons[a].append(b)

ans = 0
for v in pigeons:
    if len(v) <= 0:
        continue
    cnt = 0
    for i in range(len(v) - 1):
        if v[i] != v[i+1]:
            cnt += 1
    ans += cnt

print(ans)