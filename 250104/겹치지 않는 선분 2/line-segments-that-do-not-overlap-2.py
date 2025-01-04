import sys

'''
n개의 선분
다른 선분과 전혀 겹치지 않는 선분의 수를 출력하는.
(x1, 0), (x2, 1)
'''

n = int(input())

x1s = []
x2s = []
cnt = 0
dic = {}

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1s.append(x1)
    x2s.append(x2)

    dic[x1] = x2

x1s.sort()
x2s.sort()

# print(x1s)

for i in range(n):
    if dic[x1s[i]] == x2s[i]:
        # print(x1s[i], x2s[i])
        cnt += 1

print(cnt)