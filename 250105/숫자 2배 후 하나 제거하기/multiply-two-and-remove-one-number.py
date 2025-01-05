import sys

n = int(input())
a = list(map(int, input().split()))

min_diff = sys.maxsize

for i in range(n):
    a[i] *= 2

    for j in range(n):
        remaining_arr = a.copy()
        del remaining_arr[j]
        
        sum_diff = 0
        for k in range(n-2):
            sum_diff += abs(remaining_arr[k] - remaining_arr[k+1])

        min_diff = min(min_diff, sum_diff)

    a[i] //= 2

print(min_diff)