import sys

'''
한 명이라도 일하고 있으면 '운행되고 있는 시간'
정확히 한 명 해고, 운행되고 있는 시간 최대로
[A,B)
'''

n = int(input())
a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = -sys.maxsize


for i in range(n):
    workTime = [0 for _ in range(1001)]
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        
        x1, x2 = a[j]
        for k in range(x1, x2):
            workTime[k] += 1
        
    for v in workTime:
        if v > 0:
            cnt += 1
    ans = max(cnt, ans)

print(ans)