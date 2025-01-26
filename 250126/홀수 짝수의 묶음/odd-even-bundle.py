import sys

n = int(input())

a = list(map(int, input().split()))

even_nums = []
odd_nums = []

a.sort()

for i in range(n):
    if a[i] % 2 == 0 :
        even_nums.append(a[i])
    else:
        odd_nums.append(a[i])

print(even_nums)
print(odd_nums)

i, j = 0, 0
even_or_odd = 0 # 0: even, 1: odd

ans_list = []

while i + j <= n:
    prefix_sum = 0
    if even_or_odd == 0:
        if i + 1 < len(even_nums):
            prefix_sum += even_nums[i] + even_nums[i+1]
            i += 2
        elif j + 1 < len(odd_nums):
            prefix_sum += odd_nums[j] + odd_nums[j+1]
            j += 2
    # else:
    #     if i < len(even_nums) and j < len(odd_nums):
    #         prefix_sum += even_nums[i] + odd_nums[j]
    #         i += 1
    #         j += 1

    even_or_odd += 1
    even_or_odd = (even_or_odd % 2)    
    ans_list.append(prefix_sum)

print(ans_list)