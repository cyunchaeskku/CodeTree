import sys

n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

# Write your code here!

ans = -sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        if num[i] == num[j] and abs(j-i) <= k:
            ans = max(ans, num[i])


if ans == -sys.maxsize:
    print(-1)
else:
    print(ans)