import sys

max_ans = -sys.maxsize

n, k = map(int, input().split())

a = [0 for _ in range(10_000)]

for i in range(n):
    index, alphabet = input().split()
    a[int(index) - 1] = alphabet

for i in range(10_000 - k ):
    sum = 0
    for j in range(i, i + k + 1):
        if a[j] == 'G':
            sum += 1
        if a[j] == 'H':
            sum += 2
    max_ans = max(max_ans, sum)

print(max_ans)
'''
8 9
10 - 1
'''