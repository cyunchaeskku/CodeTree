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
        for j in range(a[i] - avg + 1):
            if a[i] <= avg:
                break
            a[i] -= 1
            ans += 1
            for k in range(n):
                if k == i:
                    continue
                elif a[k] < avg:
                    a[k] += 1
                    break

print(ans)