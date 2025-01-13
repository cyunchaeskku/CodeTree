import sys

n,m = map(int, input().split())
a = list(map(int, input().split()))

MAX_A = 10_000
ans = sys.maxsize

for i in range(MAX_A + 1): # 구간 합의 최댓값이 i일때, section 나누어지는 판단한다.
    possible = True
    section = 1

    cnt = 0

    for j in range(n):
        if a[j] > i:
            possible = False
            break
        if cnt + a[j] > i:
            cnt = 0
            section += 1
        cnt += a[j]
    if possible and section <= m:
        ans = min(ans, i)
print(ans)