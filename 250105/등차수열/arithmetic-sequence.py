import sys

n = int(input())
a = list(map(int, input().split()))


min_val = min(a)
max_val = max(a)



ans = -sys.maxsize
for k in range(1, 101): # from 1 to 100
    cnt = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (k - a[i] == a[j] - k) and k != a[i] and k != a[j]:
                cnt +=1
    ans = max(cnt, ans)
print(ans)
