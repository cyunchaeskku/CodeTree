import sys

a = list(map(int, input().split()))

a.sort()

A = min(a)
a.remove(A)
B = min(a)
C = max(a) - min(a) - B

print(A, B, C)