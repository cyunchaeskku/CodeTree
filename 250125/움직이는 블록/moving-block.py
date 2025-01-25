import sys

n = int(input())

a = [
    int(input())
    for _ in range(n)
]

def find_min_idx(a):
    min_val = sys.maxsize
    min_idx = 0
    n = len(a)

    for i in range(n):
        if a[i] < min_val:
            min_val = a[i]
            min_idx = i

    return min_idx


avg = sum(a) / n
ans = 0

for i in range(n):
    while a[i] > avg:
        idx = find_min_idx(a)
        # a[idx] += (avg - a[idx])
        # a[i] -= (avg - a[idx])
        # ans += (avg - a[idx])

        a[i] -= 1
        a[idx] += 1
        ans += 1
        
print(ans)