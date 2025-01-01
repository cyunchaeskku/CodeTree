import sys

n, b = map(int, input().split())
a = [
    int(input())
    for _ in range(n)
]

ans = -sys.maxsize

for i in range(n):
    price = 0
    cnt = 0
    for j in range(n):
        if i == j:
            a[j] /= 2

        for k in range(n):
            price += a[k]
            if price > b:
                break
            else:
                cnt += 1

        if i == j:
            a[j] *= 2
    ans = max(ans, cnt)
        
print(ans)