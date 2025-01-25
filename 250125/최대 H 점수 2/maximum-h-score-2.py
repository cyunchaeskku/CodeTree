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

for h in range(101):
    ar = a.copy()
    ar.sort(reverse=True)
    count = 0

    indicies = [False for _ in range(n)]

    for i, v in enumerate(ar):
        if v >= h:
            indicies[i] = True
    
    for i, v in enumerate(ar):
        if indicies[i] == False and v < h and count < l:
            ar[i] += 1
            indicies[i] = True
            count += 1
        if count >= l:
            break
    
    ans = max(ans, calc_H_score(ar))
    
print(ans)