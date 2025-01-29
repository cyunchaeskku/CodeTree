import sys

n, m, k = map(int, input().split())
students = [0 for _ in range(n+1)]

for i in range(m):
    v = int(input())
    students[v] += 1
    if students[v] >= k:
        print(v)
        break