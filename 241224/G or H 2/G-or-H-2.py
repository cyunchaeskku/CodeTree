import sys

n = int(input())

a= [0 for _ in range(100)]

for i in range(n):
    index, alphabet = input().split()
    a[int(index)-1] = alphabet

max_size = 0

for i in range(100):
    for j in range(i, 100):
        if a[i] == 0 or a[j] == 0:
            continue
        a_subarr = a[i:j+1]
        G_count = 0
        H_count = 0
        for v in a_subarr:
            if v == 'G':
                G_count += 1
            if v == 'H':
                H_count += 1
        if G_count == 0 or H_count == 0 or G_count == H_count:
            max_size = max(max_size, j - i)

print(max_size)