import sys

n = int(input())
_a = list(map(int, list(input().strip())))

ans = -sys.maxsize

for i in range(n):
    if _a[i] == 1:
        continue
    a = _a.copy()
    dist = sys.maxsize
    
    a[i] = 1

    for j in range(n):
        if a[j] == 1:
            for k in range(j+1, n):
                if a[k] == 1:
                    dist = min(dist, k-j)
                    break

    ans = max(dist, ans)

    
print(ans)


    