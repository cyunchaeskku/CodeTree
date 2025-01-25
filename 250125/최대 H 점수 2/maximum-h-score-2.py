import sys

n, l = map(int, input().split())

a = list(map(int, input().split()))

ans = -sys.maxsize

def calc_H_score(a):
    res = 0
    for h in range(0, max(a)+1):
        cnt = 0
        for v in a:
            if v >= h:
                cnt += 1
        if cnt >= h:
            res = max(res, h)
    return res

a.sort()
if l == 0:
    ans = max(ans, calc_H_score(a))
else:
    cnt = 0
    for i in range(len(a)):
        if a[i] >= calc_H_score(a):
            for j in range(i, i + l):
                a[j] += 1
    ans = max(ans, calc_H_score(a))
print(ans)