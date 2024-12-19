import sys

n = int(input())

a = []

for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

max_cnt = -sys.maxsize

for i in range(n):
    for j in range(n-2):
        max_cnt = max(max_cnt, a[i][j] + a[i][j+1], a[i][j+2])

print(max_cnt)