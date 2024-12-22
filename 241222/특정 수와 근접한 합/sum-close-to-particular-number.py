import sys

s, n = map(int, input().split())

a = list(map(int, input().split()))

min_ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1, n):
        for k in range(n):
            if k == i or k == j:
                continue
            else:
                sum += a[k]
        sum_diff = abs(s - sum)
        min_ans = min(min_ans, sum_diff)

print(min_ans)