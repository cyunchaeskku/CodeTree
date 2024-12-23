import sys

n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()

ans = 0 

for i in range(n - m + 1):
    a_subarr = a[i:i+m]
    a_subarr.sort()
    # print(a_subarr)

    if a_subarr == b:
        ans += 1

print(ans)