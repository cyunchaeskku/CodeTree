import sys

ans = 0

n = int(input())
a = list(map(int, input().split()))

# print(a[1:1])

for i in range(n):
    for j in range(i,n):
        avg = sum(a[i:j+1]) / (j-i+1)
        if avg % 1 == 0 and avg in a[i:j+1]:
            ans += 1

print(ans)