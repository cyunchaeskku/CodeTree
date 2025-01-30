n = int(input())
a = [
    int(input())
    for _ in range(n)
]

MAX_A = 10_000

avg = int(sum(a) / n)
ans = 0

for i in range(n):
    if a[i] > avg:
        ans += a[i] - avg
print(ans)
