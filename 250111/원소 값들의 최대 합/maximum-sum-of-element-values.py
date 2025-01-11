import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = -sys.maxsize

for i in range(len(a)-1):
    sum = 0
    pos = i
    sum += a[pos]
    for j in range(m-1):
        pos = a[pos] - 1
        sum += a[pos]
    ans = max(ans, sum)

print(ans)