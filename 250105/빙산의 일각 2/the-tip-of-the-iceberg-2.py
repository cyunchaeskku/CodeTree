import sys

n = int(input())

a= []

for _ in range(n):
    a.append(int(input()))

max_val = max(a)

ans = -sys.maxsize

for h in range(1, max_val): # from 1 to max_val-1
    cnt = 0 # 덩어리 개수
    for i in range(len(a)):
        if i > 0:
            if a[i] > h:
                if a[i-1] <= h:
                    cnt += 1
        if i == 0:
            if a[i] > h:
                cnt += 1
        ans = max(ans, cnt)

print(ans)