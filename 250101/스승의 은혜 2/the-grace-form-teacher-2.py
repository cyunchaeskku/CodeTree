import sys

n, b = map(int, input().split())
_a = [
    int(input())
    for _ in range(n)
]

_a.sort()

ans = -sys.maxsize

for i in range(n):
    for j in range(n):
        price = 0
        cnt = 0
        if i != j:
            continue
        if i == j:
            # _a[j] /= 2
            _a[j] = int(_a[j]/2)
        a = sorted(_a)

        for k in range(n):
            price += a[k]
            if price > b:
                break
            else:
                cnt += 1
        if i == j:
            # _a[j] *= 2
            _a[j] = int(_a[j]*2)
    ans = max(ans, cnt)
        
print(ans)