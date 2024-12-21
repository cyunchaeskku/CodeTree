import sys

n = int(input())

a = list(map(int, input().split()))

max_ans = -sys.maxsize

for i in range(n-2):
    for j in range(i+2, n):
        sum = a[i] + a[j]
        max_ans = max(max_ans, sum)

print(max_ans)