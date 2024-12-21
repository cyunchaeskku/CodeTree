import sys

n = int(input())

a = []

for i in range(n):
    a.append(int(input()))

min_length = sys.maxsize

cnt = 0

for i in range(n): # i에서 시작한다면
    length = 0
    cnt = 0
    # print("i:", i)
    # for j in range(0, i):
    #     length += a[j] * (n - j - 1)
    # for j in range(i,n):
    #     length += a[j] * (j - i)

    for j in range(i, n):
        length += a[j] * cnt
        cnt += 1
    for j in range(0, i):
        # print(cnt)
        length += a[j] * cnt
        cnt += 1

    min_length = min(min_length, length)
    # print(length)

print(min_length)

'''
i = 1
a[1] * (1 - i) 0
a[2] * (2 - i) 1
a[3] * (3 - i) 2
a[4] * (4 - i) 3
a[0] * (n - 0 - 1) 4

i = 2
a[2] * (2 - i) 0
a[3] * (3 - i) 1
a[4] * (4 - i) 2
a[0] * (n - 0 - 1) 4
a[1] * (n - 1 - 1) 3
'''