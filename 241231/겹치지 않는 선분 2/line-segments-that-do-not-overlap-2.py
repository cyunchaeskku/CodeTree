import sys

'''
n개의 선분
다른 선분과 전혀 겹치지 않는 선분의 수를 출력하는.
(x1, 0), (x2, 1)

안 겹치려면, x2와 x1사이에 다른 x1, x2가 있으면 안 됨.
'''

n = int(input())

# x1s = []
# x2s = []
cnt = 0

# for _ in range(n):
#     x1, x2 = map(int, input().split())
#     x1s.append(x1)
#     x2s.append(x2)

a = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

a.sort()

for i in range(n):

    if i == 0:
        if a[i][1] < a[i+1][1]:
            cnt += 1
    elif i == n-1:
        if a[i][0] > a[i-1][0]:
            cnt += 1
    else:
        if a[i][1] > a[i-1][1] and a[i][1] < a[i+1][1]:
            cnt += 1

print(cnt)

