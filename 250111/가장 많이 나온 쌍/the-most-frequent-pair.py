import sys

n, m = map(int, input().split())

segments = [
    list(map(int, input().split()))
    for _ in range(m)
]

for li in segments:
    li.sort()

ans = -sys.maxsize

for i in range(n+1):
    for j in range(i+1, n+1):
        cnt = 0

        for li in segments:
            if li == [i,j]:
                cnt += 1
            

        ans = max(ans, cnt)
print(ans)