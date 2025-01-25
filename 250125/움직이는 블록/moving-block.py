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

ar = a.copy()    

avg = sum(a) / n
ans = 0

for i in range(n):
    while a[i] > avg:
        a[i] -= 1
        a[find_min_idx(a)] += 1
        ans += 1
print(ans)