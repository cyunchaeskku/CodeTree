import sys

n = int(input())
a = list(map(int, input().split()))

min_val = min(a)

ar = []
for i in range(len(a)):
    if a[i] > min_val:
        ar.append(a[i])

if len(ar) == 0:
    print(-1)
    exit(0)

ans = sys.maxsize
val = sys.maxsize
flag = False
for i in range(n):
    if a[i] == min(ar):
        ans = i + 1
        val = a[i]
        flag = True
        break

if flag == False:
    print(-1)
elif a.count(val) > 1:
    print(-1)
else:
    print(ans)
