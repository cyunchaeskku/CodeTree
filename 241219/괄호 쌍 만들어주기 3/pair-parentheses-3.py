import sys

a = list(input().rstrip())

cnt = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == '(' and a[j] == ')':
            cnt += 1
print(cnt)