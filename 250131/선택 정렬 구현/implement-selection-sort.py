import sys

n = int(input())
a = list(map(int, input().split()))

def selection_sort(n, a):
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a

a = selection_sort(n, a)

for v in a:
    print(v, end= ' ')