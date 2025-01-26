import sys

a = list(map(int, input().split()))

a.sort()

A = a[0]
B = a[1]
C = a[len(a) - 1] - A - B

print(A, B, C)