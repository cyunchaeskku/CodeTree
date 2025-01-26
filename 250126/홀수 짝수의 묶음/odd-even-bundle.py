import sys

n = int(input())

a = list(map(int, input().split()))

even_nums = []
odd_nums = []


for i in range(n):
    if a[i] % 2 == 0 :
        even_nums.append(a[i])
    else:
        odd_nums.append(a[i])

i, j = 0, 0
even_or_odd = 0 # 0: even, 1: odd

ans_list = []
ans = 0

while True:
    if even_or_odd == 0: #even number
        if len(odd_nums) == 0:
            ans_list.append(even_nums)
            even_nums = []
            ans += 1
        elif len(even_nums) > 0:
            if len(even_nums) == 1:
                if len(odd_nums) == 2:
                    ans += 1
                    even_nums = []
                    odd_nums = []
                else:
                    val = even_nums.pop()
                    ans_list.append([val])
                    ans += 1        
            else:
                val = even_nums.pop()
                ans_list.append([val])
                ans += 1
        # 남은 짝수가 더 없을 때
        else:
            if len(odd_nums) >= 2:
                val1 = odd_nums.pop()
                val2 = odd_nums.pop()
                ans_list.append([val1,val2])
                ans += 1
                
    else: #odd number
        if len(odd_nums) > 0:
            if len(odd_nums) == 5:
                val1 = odd_nums.pop()
                val2 = odd_nums.pop()
                val3 = odd_nums.pop()
                ans_list.append([val1, val2, val3])
                ans += 1
            else:
                val = odd_nums.pop()
                ans_list.append([val])
                ans += 1
           
           

    even_or_odd += 1
    even_or_odd = even_or_odd % 2
    if len(even_nums) == 0 and len(odd_nums) == 0:
        break

print(ans)