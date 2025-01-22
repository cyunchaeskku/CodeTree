import sys

n, m, p = map(int, input().split())

programmers = [False for _ in range(n)]

'''
A = 65
'''

appeared_chrs = set()

for i in range(m):
    c, u = input().split()
    appeared_chrs.add(c)
    idx = ord(c) - 65
    if i >= p - 1:
        programmers[idx] = True
    if u == 0:
        for v in appeared_chrs:
            programmers[ord(v) - 65] = True


for i, v in enumerate(programmers):
    if v == False:
        print(chr(i + 65), end = ' ')