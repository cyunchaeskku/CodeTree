import sys

n, m, k = map(int, input().split())
students = [0 for _ in range(n+1)]

flag= False
for i in range(m):
    v = int(input())
    students[v] += 1
    if students[v] >= k:
        if flag == False:
            flag = True
            print(v)
        
if flag == False:
    print(-1)