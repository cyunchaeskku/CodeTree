import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = -sys.maxsize

for i in range(len(a)-1):
    su = 0
    pos = i
    su += a[pos]
    for j in range(m-1):
        pos = a[pos] - 1
        su += a[pos]
    ans = max(ans, su)

print(ans)


'''
5
a[5-1] = 3
a[3-1] = 4
a[4-1] = 2
'''