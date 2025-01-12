import sys

n, k = map(int, input().split())

arr = [
    int(input())
    for _ in range(n)
]

bomb_numbers = set()
for v in arr:
    bomb_numbers.add(v)
bomb_numbers = list(bomb_numbers)

ans = 0
max_boom_count = 0

for v in bomb_numbers:
    ar = arr.copy()
    boom_count = 0
    
    for i in range(n):
        if_boom = False
        if ar[i] == v:
            for j in range(i+1, n):
                if ar[j] == v and abs(j - i) <= k:
                    if_boom = True
                    break
        if if_boom:
            boom_count += 1
    if max_boom_count < boom_count:
        ans = v
        max_boom_count = boom_count
if max_boom_count == 0:
    print(0)
else:
    print(ans)