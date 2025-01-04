import sys

n, c, g, h = map(int, input().split())

tAs = []
tBs = []

ans = -sys.maxsize

min_temp, max_temp = sys.maxsize, -sys.maxsize

for _ in range(n):
    ta, tb = map(int, input().split())
    tAs.append(ta)
    tBs.append(tb)

    min_temp = min(min_temp, ta)
    max_temp = max(max_temp, tb)

for temp in range(min_temp-10, max_temp+10):
    work = 0
    
    for i in range(n):
        if temp < tAs[i]:
            work += c
        if temp >= tAs[i] and temp < tBs[i]:
            work += g
        if temp >= tBs[i]:
            work += h

    ans = max(ans, work)

print(ans)