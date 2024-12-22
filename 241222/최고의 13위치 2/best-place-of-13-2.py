import sys

n = int(input())

a = []

max_ans = 0

for i in range(n):
    a.append( list(map(int, input().split())) )

for i in range(n-1):
    for j in range(n-2):
        for k in range(i+1, n):
            for l in range(n-2):
                sum = a[i][j] + a[i][j+1] + a[i][j+2] + a[k][l] + a[k][l+1] + a[k][l+2]
                max_ans = max (max_ans, sum)

for i in range(n):
    for j in range(n-4):
        for l in range(j+1, n-2):
            sum = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][l] + a[i][l+1] + a[i][l+2]
            max_ans = max (max_ans, sum)

            
print(max_ans)