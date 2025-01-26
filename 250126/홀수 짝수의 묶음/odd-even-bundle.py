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
    if even_or_odd == 0:
        if len(even_nums) > 0:
            ans_list.append([even_nums.pop()])
            ans += 1
        elif len(odd_nums) >= 2:
            val1 = odd_nums.pop()
            val2 = odd_nums.pop()
            ans_list.append([val1, val2])
            ans += 1
        else:
            # if len(even_nums) > 0 or len(odd_nums) > 0:
            ans -= 1
            break
    else:
        if len(odd_nums) > 0:
            ans_list.append([odd_nums.pop(0)])
            ans += 1
        else:
            break
    
    even_or_odd = (even_or_odd + 1) % 2
    if len(even_nums) == 0 and len(odd_nums) == 0:
        break

print(ans)