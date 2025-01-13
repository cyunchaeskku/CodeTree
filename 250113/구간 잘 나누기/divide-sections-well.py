import sys

n, m = map(int, input().split())
arr = list()
temp = list(map(int, input().split()))

for i in range(n):
    arr.append(temp[i])
    arr.append(0)

del arr[2 * n - 1]


ans = sys.maxsize

# arr의 길이는 2 * n - 1

for i in range(2 * n - 1):
    for j in range(i + 1, 2 * n - 1):
        ar = arr.copy()

        range_sum = 0
        max_range_sum = -sys.maxsize

        if ar[i] > 0 or ar[j] > 0:
            continue
        ar[i], ar[j] = -1, -1



        for k in range(2 * n - 1):
            if ar[k] > - 1:
                range_sum += ar[k]
            if ar[k] == -1:
                max_range_sum = max(max_range_sum, range_sum)
                range_sum = 0
        max_range_sum = max(range_sum, max_range_sum)
        ans = min(ans, max_range_sum)

print(ans)
