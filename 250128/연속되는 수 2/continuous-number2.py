import sys

n = int(input())

a = [
    int(input())
    for _ in range(n)
]

cnt = 0
ans  = -sys.maxsize

for i in range(n):
    if i > 0:
        if a[i] != a[i - 1]:
            ans = max(ans, cnt)
            cnt = 1
        else:
            cnt += 1
    else:
        cnt = 1
    

print(ans)