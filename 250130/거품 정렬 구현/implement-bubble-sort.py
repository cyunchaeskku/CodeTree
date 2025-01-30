import sys

n = int(input())

a = list(map(int, input().split()))

def bubble_sort(a, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


ar = bubble_sort(a, n)
for v in ar:
    print(v, end=' ')