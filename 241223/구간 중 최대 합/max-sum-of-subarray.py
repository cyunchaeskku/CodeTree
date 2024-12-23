import sys

n , k = map(int, input().split())
a = list(map(int, input().split()))

max_ans = -sys.maxsize

for i in range(n - k + 1):
    sum = 0
    for j in range(i, i+k):
        sum += a[j]
    max_ans = max(max_ans, sum)
print(max_ans)