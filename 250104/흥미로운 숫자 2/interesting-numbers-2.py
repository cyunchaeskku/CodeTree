import sys

x, y = map(int, input().split())

ans = 0

for n in range(x, y+1):
    num_list = list(str(n))

    onlyTwoKinds = True # 두 종료의 숫자만 들어있는가
    onlyOne = True # 정확히 한 자리만 다른 숫자

    nums = [0 for _ in range(10)]

    for i in range(len(num_list)):
        nums[int(num_list[i])] += 1

    # print(nums)

    notZeroCnt = 0
    for v in nums:
        if v > 0:
            notZeroCnt += 1
    if notZeroCnt != 2:
        continue
    
    temp_cnt = 0
    a, b = 0, 0
    for i in range(len(nums)):
        if nums[i] > 0:
            if temp_cnt == 0:
               a = nums[i]
               temp_cnt += 1
            else:
                b = nums[i]

    if (a > 1 and b > 1):
        continue
    else:
        ans += 1

print(ans)
