import sys

n = int(input())
a = list(map(int,input().split()))

min_len = sys.maxsize

for i in range(n):
    length = 0
    for j in range(n):
        length += a[j] * abs(j-i)
        # print(length)
    if length < min_len:
        min_len = length

print(min_len)