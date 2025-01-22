import sys

'''
각 사람의 이동 거리의 합 중 최소를 구하라
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for i in range(len(a) -1, 0, - 1):
    if a[i] < b[i]:
        for j in range(i-1, -1, - 1):
            if a[i] == b[i]:
                break
            val = min(a[j], b[i] - a[i])
            cnt += val * abs(i-j)
            print(val)
            a[j] -= val
            a[i] += val
    else:
        continue

print(cnt)