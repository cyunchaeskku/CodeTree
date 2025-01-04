import sys

k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]


# Write your code here!

nums = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


for i in range(1, n+1):
    for v in arr:
        i_index = -1
        for j in range(n):
            if v[j] == i:
                i_index = j
        for j in range(n):
            if j > i_index:
                nums[i][v[j]] += 1


ans = 0
for i in range(n+1):
    for j in range(n+1):
        if nums[i][j] == k:
            ans += 1

# print(nums)
print(ans)