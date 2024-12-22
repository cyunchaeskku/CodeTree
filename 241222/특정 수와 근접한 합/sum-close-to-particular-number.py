import sys

n, s = map(int, input().split())

a = list(map(int, input().split()))

min_ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1, n):
        sum_ans = sum(a) - a[i] - a[j]
        sum_diff = abs(s - sum_ans)
        min_ans = min(min_ans, sum_diff)

print(min_ans)