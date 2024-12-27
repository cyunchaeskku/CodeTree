import sys

a = list(map(int, input().split()))

def get_diff(i, j, k):
    sum_a = a[i] + a[j] + a[k]
    sum_total = sum(a)
    return abs((sum_total - sum_a) - sum_a)

min_diff = sys.maxsize

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            min_diff = min(min_diff, get_diff(i,j,k))


print(min_diff)