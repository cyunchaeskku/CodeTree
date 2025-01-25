import sys

n = int(input())

a = [
    int(input())
    for _ in range(n)
]

avg = int(sum(a) / n)
ans = 0


# for i in range(n):
#     if a[i] > avg:
#         val = a[i] - avg
#         a[i] -= val
#         a[a.index(min(a))] += val
#         ans += val
#     elif a[i] < avg:
#         val = avg - a[i]
#         a[i] += val
#         a[a.index(max(a))] -= val
#         ans += val

for v in a:
    if v > avg:
        ans += v - avg
print(ans)