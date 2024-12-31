import sys

n = int(input())

a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x,y))

ans = sys.maxsize


for i in range(n):
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = -sys.maxsize, -sys.maxsize
    for j in range(n):
        if i == j:
            continue
        
        x, y = a[j]
        min_x, min_y = min(x, min_x), min(y, min_y)
        max_x, max_y = max(x, max_x), max(y, max_y)

    ans = min(ans, (max_x - min_x) * (max_y - min_y))
    
print(ans)