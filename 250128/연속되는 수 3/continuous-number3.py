import sys

n = int(input())
a = [
    int(input())
    for _ in range(n)
]

cnt = 0
ans = - sys.maxsize
prev_sign = 1 # 1: plus, -1: minus, 0: zero

for i in range(n):
    if i == 0:
        cnt = 1
        if a[i] < 0:
            prev_sign = -1
        elif a[i] == 0:
            prev_sign = 0
        elif a[i] > 0:
            prev_sign = 1
    else:
        if a[i] < 0:
            cur_sign = - 1
        elif a[i] == 0:
            cur_sign = 0
        elif a[i] > 0:
            cur_sign = 1
        if cur_sign != prev_sign:
            ans = max(ans, cnt)
            prev_sign = cur_sign
            cnt = 1
        else:
            cnt += 1
ans = max(cnt, ans)
print(ans)