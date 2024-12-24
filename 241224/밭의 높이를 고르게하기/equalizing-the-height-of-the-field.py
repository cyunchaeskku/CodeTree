import sys

n, h, t = map(int, input().split())

a  = list(map(int, input().split()))

min_cost = sys.maxsize

for i in range(n):
    for j in range(i,n):
        if j-i+1 < t:
            continue
        a_subarr = a[i:j+1]
        cost = 0
        for v in a_subarr:
            if v < h:
                cost += abs(h - v)
            if v > h:
                cost += abs(h-v)
        min_cost = min(cost, min_cost)

print(min_cost)